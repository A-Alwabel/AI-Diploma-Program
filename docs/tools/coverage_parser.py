#!/usr/bin/env python3
"""
Parse DETAILED_UNIT_DESCRIPTIONS.md and cross-check with repository structure.
Generate coverage map report.
"""

import re
import json
import os
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Base directory
BASE_DIR = Path(__file__).parent.parent

def parse_detailed_descriptions():
    """Parse DETAILED_UNIT_DESCRIPTIONS.md into structured format."""
    desc_file = BASE_DIR / "DETAILED_UNIT_DESCRIPTIONS.md"
    
    if not desc_file.exists():
        raise FileNotFoundError(f"Could not find {desc_file}")
    
    with open(desc_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    curriculum = {}
    current_course = None
    current_unit = None
    
    # Pattern to match course headers
    course_pattern = r"## 📘 COURSE (\d+): (.+?)$"
    # Pattern to match unit headers
    unit_pattern = r"#### 📖 Unit (\d+): (.+?) \((\d+) hours: (\d+) theory \+ (\d+) practical\)"
    
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check for course header
        course_match = re.match(course_pattern, line)
        if course_match:
            course_num = int(course_match.group(1))
            course_name = course_match.group(2).strip()
            
            # Get Arabic name from next line if it exists
            course_arabic = ""
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("**"):
                course_arabic = lines[i + 1].strip().replace("**", "").strip()
                i += 1
            
            current_course = f"Course {course_num:02d}"
            curriculum[current_course] = {
                "number": course_num,
                "name": course_name,
                "arabic_name": course_arabic,
                "units": {}
            }
            current_unit = None
            i += 1
            continue
        
        # Check for unit header
        unit_match = re.match(unit_pattern, line)
        if unit_match and current_course:
            unit_num = int(unit_match.group(1))
            unit_name = unit_match.group(2).strip()
            total_hours = int(unit_match.group(3))
            theory_hours = int(unit_match.group(4))
            practical_hours = int(unit_match.group(5))
            
            current_unit = f"Unit {unit_num}"
            curriculum[current_course]["units"][current_unit] = {
                "number": unit_num,
                "name": unit_name,
                "hours": {
                    "total": total_hours,
                    "theory": theory_hours,
                    "practical": practical_hours
                },
                "theoretical_topics": [],
                "practical_activities": []
            }
            i += 1
            continue
        
        # Check for theoretical content section
        if "**Theoretical Content:**" in line and current_unit:
            i += 1
            topics = []
            while i < len(lines) and "**Practical Content:**" not in lines[i]:
                line = lines[i].strip()
                if line and not line.startswith("#") and not line.startswith("---"):
                    # Check if it's a numbered topic
                    if re.match(r"^\d+\.", line):
                        topics.append(line)
                i += 1
            curriculum[current_course]["units"][current_unit]["theoretical_topics"] = topics
            continue
        
        # Check for practical content section
        if "**Practical Content:**" in line and current_unit:
            i += 1
            activities = []
            while i < len(lines) and not lines[i].startswith("---") and not lines[i].startswith("####"):
                line = lines[i].strip()
                if line and line.startswith("-"):
                    activities.append(line[1:].strip())
                i += 1
            curriculum[current_course]["units"][current_unit]["practical_activities"] = activities
            continue
        
        i += 1
    
    return curriculum

def discover_repository_structure():
    """Discover actual repository structure."""
    structure = {}
    
    # Find all course directories
    for course_dir in sorted(BASE_DIR.glob("Course *")):
        if not course_dir.is_dir():
            continue
        
        # Extract course number
        match = re.match(r"Course (\d+)", course_dir.name)
        if not match:
            continue
        
        course_num = int(match.group(1))
        course_key = f"Course {course_num:02d}"
        
        structure[course_key] = {
            "path": str(course_dir.relative_to(BASE_DIR)),
            "exists": True,
            "units": {},
            "notebooks": []
        }
        
        # Find unit directories
        unit_dirs = list(course_dir.glob("unit*"))
        for unit_dir in sorted(unit_dirs):
            if not unit_dir.is_dir():
                continue
            
            # Extract unit number and name
            match = re.match(r"unit(\d+)-(.+)", unit_dir.name)
            if match:
                unit_num = int(match.group(1))
                unit_name = match.group(2)
                unit_key = f"Unit {unit_num}"
                
                structure[course_key]["units"][unit_key] = {
                    "path": str(unit_dir.relative_to(BASE_DIR)),
                    "name": unit_name,
                    "exists": True,
                    "notebooks": {
                        "examples": [],
                        "exercises": []
                    }
                }
                
                # Find notebooks in examples/
                examples_dir = unit_dir / "examples"
                if examples_dir.exists():
                    for nb in examples_dir.glob("*.ipynb"):
                        structure[course_key]["units"][unit_key]["notebooks"]["examples"].append(
                            str(nb.relative_to(BASE_DIR))
                        )
                
                # Find notebooks in exercises/
                exercises_dir = unit_dir / "exercises"
                if exercises_dir.exists():
                    for nb in exercises_dir.glob("*.ipynb"):
                        structure[course_key]["units"][unit_key]["notebooks"]["exercises"].append(
                            str(nb.relative_to(BASE_DIR))
                        )
        
        # Also check for course-specific notebook locations (e.g., Course 02/NOTEBOOKS/)
        notebooks_dir = course_dir / "NOTEBOOKS"
        if notebooks_dir.exists():
            for nb in notebooks_dir.glob("*.ipynb"):
                structure[course_key]["notebooks"].append(str(nb.relative_to(BASE_DIR)))
        
        # Find all notebooks in course directory recursively
        for nb in course_dir.rglob("*.ipynb"):
            rel_path = str(nb.relative_to(BASE_DIR))
            if rel_path not in structure[course_key]["notebooks"]:
                # Check if it's already in a unit
                in_unit = False
                for unit_info in structure[course_key]["units"].values():
                    if rel_path in unit_info["notebooks"]["examples"] or rel_path in unit_info["notebooks"]["exercises"]:
                        in_unit = True
                        break
                if not in_unit:
                    structure[course_key]["notebooks"].append(rel_path)
    
    return structure

def generate_coverage_report(curriculum, structure):
    """Generate coverage map report."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "summary": {
            "total_courses_curriculum": len(curriculum),
            "total_courses_repo": len(structure),
            "total_units_curriculum": sum(len(c["units"]) for c in curriculum.values()),
            "total_units_repo": sum(len(c["units"]) for c in structure.values()),
            "total_notebooks": sum(
                len(c["notebooks"]) + 
                sum(len(u["notebooks"]["examples"]) + len(u["notebooks"]["exercises"]) 
                    for u in c["units"].values())
                for c in structure.values()
            )
        },
        "courses": {}
    }
    
    # Check each course
    all_courses = set(curriculum.keys()) | set(structure.keys())
    
    for course_key in sorted(all_courses):
        course_report = {
            "exists_in_curriculum": course_key in curriculum,
            "exists_in_repo": course_key in structure,
            "units": {}
        }
        
        if course_key in curriculum:
            course_report["curriculum_name"] = curriculum[course_key]["name"]
            course_report["curriculum_units"] = len(curriculum[course_key]["units"])
        
        if course_key in structure:
            course_report["repo_path"] = structure[course_key]["path"]
            course_report["repo_notebooks"] = len(structure[course_key]["notebooks"])
            course_report["repo_units"] = len(structure[course_key]["units"])
        
        # Check units
        curriculum_units = curriculum.get(course_key, {}).get("units", {})
        repo_units = structure.get(course_key, {}).get("units", {})
        
        all_units = set(curriculum_units.keys()) | set(repo_units.keys())
        
        for unit_key in sorted(all_units):
            unit_report = {
                "exists_in_curriculum": unit_key in curriculum_units,
                "exists_in_repo": unit_key in repo_units,
            }
            
            if unit_key in curriculum_units:
                unit_info = curriculum_units[unit_key]
                unit_report["curriculum_name"] = unit_info["name"]
                unit_report["curriculum_topics"] = len(unit_info["theoretical_topics"])
                unit_report["curriculum_practical"] = len(unit_info["practical_activities"])
            
            if unit_key in repo_units:
                unit_info = repo_units[unit_key]
                unit_report["repo_path"] = unit_info["path"]
                unit_report["repo_examples"] = len(unit_info["notebooks"]["examples"])
                unit_report["repo_exercises"] = len(unit_info["notebooks"]["exercises"])
                unit_report["repo_notebooks"] = (
                    len(unit_info["notebooks"]["examples"]) + 
                    len(unit_info["notebooks"]["exercises"])
                )
            
            course_report["units"][unit_key] = unit_report
        
        report["courses"][course_key] = course_report
    
    return report

def main():
    """Main execution."""
    print("=" * 60)
    print("COVERAGE PARSER")
    print("=" * 60)
    
    print("\n1. Parsing DETAILED_UNIT_DESCRIPTIONS.md...")
    try:
        curriculum = parse_detailed_descriptions()
        print(f"   ✓ Found {len(curriculum)} courses")
        total_units = sum(len(c["units"]) for c in curriculum.values())
        print(f"   ✓ Found {total_units} units")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return
    
    print("\n2. Discovering repository structure...")
    try:
        structure = discover_repository_structure()
        print(f"   ✓ Found {len(structure)} course directories")
        total_units = sum(len(c["units"]) for c in structure.values())
        print(f"   ✓ Found {total_units} unit directories")
        total_notebooks = sum(
            len(c["notebooks"]) + 
            sum(len(u["notebooks"]["examples"]) + len(u["notebooks"]["exercises"]) 
                for u in c["units"].values())
            for c in structure.values()
        )
        print(f"   ✓ Found {total_notebooks} notebooks")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return
    
    print("\n3. Generating coverage report...")
    try:
        report = generate_coverage_report(curriculum, structure)
        
        # Save JSON report
        json_file = BASE_DIR / "artifacts" / "coverage_map.json"
        json_file.parent.mkdir(parents=True, exist_ok=True)
        with open(json_file, "w") as f:
            json.dump(report, f, indent=2)
        print(f"   ✓ Saved JSON report: {json_file}")
        
        # Generate markdown report
        md_file = BASE_DIR / "COVERAGE_MAP_REPORT.md"
        with open(md_file, "w") as f:
            f.write("# Coverage Map Report\n\n")
            f.write(f"**Generated:** {report['timestamp']}\n\n")
            f.write("## Summary\n\n")
            f.write(f"- **Courses in Curriculum:** {report['summary']['total_courses_curriculum']}\n")
            f.write(f"- **Courses in Repository:** {report['summary']['total_courses_repo']}\n")
            f.write(f"- **Units in Curriculum:** {report['summary']['total_units_curriculum']}\n")
            f.write(f"- **Units in Repository:** {report['summary']['total_units_repo']}\n")
            f.write(f"- **Total Notebooks:** {report['summary']['total_notebooks']}\n\n")
            
            f.write("## Course-by-Course Analysis\n\n")
            for course_key, course_info in sorted(report["courses"].items()):
                f.write(f"### {course_key}\n\n")
                if "curriculum_name" in course_info:
                    f.write(f"**Curriculum Name:** {course_info['curriculum_name']}\n\n")
                if "repo_path" in course_info:
                    f.write(f"**Repository Path:** `{course_info['repo_path']}`\n\n")
                
                f.write("**Units:**\n\n")
                for unit_key, unit_info in sorted(course_info["units"].items()):
                    f.write(f"- **{unit_key}**\n")
                    if "curriculum_name" in unit_info:
                        f.write(f"  - Curriculum: {unit_info['curriculum_name']}\n")
                        f.write(f"  - Topics: {unit_info.get('curriculum_topics', 0)}\n")
                        f.write(f"  - Practical Activities: {unit_info.get('curriculum_practical', 0)}\n")
                    if "repo_path" in unit_info:
                        f.write(f"  - Repository: `{unit_info['repo_path']}`\n")
                        f.write(f"  - Example Notebooks: {unit_info.get('repo_examples', 0)}\n")
                        f.write(f"  - Exercise Notebooks: {unit_info.get('repo_exercises', 0)}\n")
                    f.write("\n")
                f.write("\n")
        
        print(f"   ✓ Saved Markdown report: {md_file}")
        
        print("\n" + "=" * 60)
        print("COVERAGE PARSING COMPLETE")
        print("=" * 60)
        
    except Exception as e:
        print(f"   ✗ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
