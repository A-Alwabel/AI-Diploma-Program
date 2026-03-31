"""
Unit 1 - Exercise 1: Solutions
الوحدة 1 - تمرين 1: الحلول

Complete solutions to Exercise 1.
الحلول الكاملة للتمرين 1.
"""

# Solution 1: AI Definition
ai_definition = """
Artificial Intelligence (AI) is a branch of computer science that aims to 
create systems capable of performing tasks that typically require human 
intelligence, such as learning, reasoning, and problem-solving.

الذكاء الاصطناعي هو فرع من علوم الحاسوب يهدف إلى إنشاء أنظمة قادرة على
أداء مهام تتطلب عادة ذكاءً بشرياً، مثل التعلم والاستدلال وحل المشاكل.
"""

# Solution 2: System Classification
system_types = {
    "Siri voice assistant": "Narrow AI",
    "Self-driving car": "Narrow AI",
    "Chess-playing computer": "Narrow AI",
    "Human-like robot that can do any task": "General AI",
    "AI that is smarter than all humans combined": "Superintelligent AI"
}

# Solution 3: AI Applications (Example: Healthcare)
chosen_field = "Healthcare"
applications = [
    "Medical image analysis for disease detection",
    "Drug discovery and development",
    "Personalized treatment recommendations"
]

# Solution 4: Movie Recommendation System
def recommend_movie(age, genre_preference, mood):
    """
    Rule-based movie recommendation system.
    """
    # Age-based restrictions
    if age < 13:
        if genre_preference == 'horror':
            return "Sorry, horror movies are not suitable for your age"
    
    # Mood-based recommendations
    if mood == 'sad':
        if genre_preference == 'comedy':
            return "Comedy movie to cheer you up!"
        else:
            return "Light drama might help"
    
    elif mood == 'excited':
        if genre_preference == 'action':
            return "Action movie to match your energy!"
        else:
            return "Any genre works when you're excited"
    
    elif mood == 'relaxed':
        return f"Enjoy a {genre_preference} movie to relax"
    
    else:  # happy
        return f"Great time for a {genre_preference} movie!"

# Test the solution
if __name__ == "__main__":
    test_cases = [
        (25, 'action', 'excited'),
        (15, 'comedy', 'happy'),
        (30, 'drama', 'sad')
    ]
    
    for age, genre, mood in test_cases:
        recommendation = recommend_movie(age, genre, mood)
        print(f"Age: {age}, Genre: {genre}, Mood: {mood}")
        print(f"Recommendation: {recommendation}\n")
