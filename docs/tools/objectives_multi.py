#!/usr/bin/env python3
"""Replace generic learning objectives with specific ones. Supports courses 01, 02, 08, 09, 10, 11, 12."""

from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

# Objectives by (course, basename) or (course, rel). Use basename (Path.stem) when same file appears in multiple paths.
def _obj(*s): return list(s)

OBJECTIVES = {
    "01": {
        "01_ai_introduction": _obj(
            "Define AI and its main goals; distinguish AI, ML, and DL",
            "Identify typical AI applications and ethical considerations",
        ),
        "02_ai_history": _obj(
            "Summarize key milestones in AI history",
            "Connect historical trends to current tools and limitations",
        ),
        "03_intelligent_agents_rationality": _obj(
            "Describe agents, environments, and rationality",
            "Classify agents by percepts, actions, and goals",
        ),
        "04_philosophy_turing_test": _obj(
            "Explain the Turing test and main philosophical debates",
            "Discuss strengths and limitations of behavioral definitions of intelligence",
        ),
        "05_adversarial_search_minimax": _obj(
            "Implement minimax and alpha–beta pruning for game trees",
            "Apply adversarial search to simple two‑player games",
        ),
        "09_case_studies_intelligent_agents": _obj(
            "Analyze real-world systems as intelligent agents",
            "Map agent design to environment and performance metrics",
        ),
        "01_bfs_algorithm": _obj("Implement BFS; trace exploration order", "Use BFS for shortest paths in unweighted graphs"),
        "02_dfs_algorithm": _obj("Implement DFS; compare with BFS", "Apply DFS for cycles, topological sort"),
        "03_astar_algorithm": _obj("Implement A* with a heuristic", "Compare A* with BFS/DFS on informed search"),
        "04_expert_systems": _obj("Design rule-based expert systems", "Implement simple inference engines"),
        "05_bayes_theorem": _obj("Apply Bayes' theorem to update probabilities", "Use prior, likelihood, and posterior in simple examples"),
        "06_machine_learning_intro": _obj("Distinguish supervised, unsupervised, and reinforcement learning", "Match problem types to ML paradigms"),
        "01_knowledge_graph": _obj("Model knowledge as graphs; use RDF-style triples", "Query and navigate knowledge graphs"),
        "02_rule_based_systems": _obj("Write and apply production rules", "Implement forward/backward chaining"),
        "03_expert_systems": _obj("Build a small expert system with rules", "Handle uncertainty in rule-based reasoning"),
        "04_regression_classification": _obj("Implement simple regression and classification models", "Use metrics (MSE, accuracy) and interpret results"),
        "05_perceptron_xor": _obj("Understand linear separability and the XOR problem", "Use multi-layer models to solve XOR"),
        "01_simple_perceptron": _obj("Implement a single-layer perceptron", "Train on linearly separable data and interpret weights"),
        "02_generative_ai_intro": _obj("Contrast generative vs discriminative models", "Recognize common generative model families"),
        "03_cnn_rnn_architectures": _obj("Describe CNN and RNN architectures and use cases", "Apply CNNs/RNNs to simple vision or sequence tasks"),
        "01_generative_ai_introduction": _obj("Define generative AI and typical applications", "Identify model types (GANs, VAEs, LMs) and trade-offs"),
        "02_generative_vs_discriminative": _obj("Compare generative vs discriminative learning", "Choose the appropriate paradigm for a given task"),
        "03_course_summary": _obj("Synthesize AI foundations, search, knowledge, and neural concepts", "Connect course topics to further study"),
        "04_diabetes_classification_ffnn": _obj("Build a feedforward classifier for a tabular dataset", "Preprocess data, train, and evaluate the model"),
    },
    "02": {
        "00_Python_Libraries_for_AI": _obj("Use NumPy, Pandas, and basic AI-related libraries", "Load data and run simple ML workflows"),
        "01_Introduction_Search_Algorithms": _obj("Implement and compare search algorithms (BFS, DFS, A*)", "Apply search to graphs and problem spaces"),
        "02_Knowledge_Representation": _obj("Represent knowledge with logic, rules, and graphs", "Implement inference and querying"),
        "03_Learning_Under_Uncertainty": _obj("Apply probability, Bayes, and decision theory", "Model uncertainty in inference and learning"),
        "04_Optimization_Techniques": _obj("Implement gradient-based optimization and variants", "Tune learning rates and compare optimizers"),
        "05_AI_Learning_Models": _obj("Build and evaluate common AI/ML models", "Compare model families and deployment considerations"),
    },
    "08": {
        "01_simple_neural_network": _obj("Implement a simple feedforward network from scratch", "Train with backpropagation and interpret loss curves"),
        "02_backpropagation_detailed": _obj("Derive and implement backpropagation", "Trace gradients through layers and activations"),
        "03_optimization_techniques": _obj("Apply SGD, momentum, Adam, and regularization", "Diagnose training and improve convergence"),
        "01_cnn_architecture": _obj("Build CNNs with convolutions and pooling", "Apply CNNs to image classification"),
        "02_cnn_advanced_architectures": _obj("Use ResNet, VGG-style, or similar architectures", "Apply transfer learning and fine-tuning"),
        "03_transfer_learning_cnns": _obj("Transfer pretrained CNNs to new tasks", "Freeze vs fine-tune layers and evaluate"),
        "01_rnn_basics": _obj("Implement RNNs and handle sequences", "Use RNNs for sequence prediction or classification"),
        "02_lstm_advanced": _obj("Use LSTMs (and optionally GRUs) for longer sequences", "Apply to text or time series"),
        "01_transformer_attention": _obj("Implement self-attention and transformer blocks", "Understand scaling and positional encodings"),
        "02_bert_finetuning": _obj("Fine-tune BERT (or similar) for downstream tasks", "Use Hugging Face or equivalent APIs"),
        "03_sequence_to_sequence": _obj("Build encoder–decoder and seq2seq models", "Apply to translation or summarization"),
        "03_gpt_text_generation": _obj("Use GPT-style models for text generation", "Control sampling and decode outputs"),
        "01_model_optimization": _obj("Apply quantization, pruning, and basic optimization", "Reduce model size and latency"),
        "02_tensorflow_serving": _obj("Serve models with TensorFlow Serving", "Deploy and query via REST/gRPC"),
        "03_onnx_conversion": _obj("Export models to ONNX and run cross-platform", "Compare runtimes and performance"),
        "04_model_pruning": _obj("Prune weights and structured sparsity", "Measure accuracy–efficiency trade-offs"),
        "05_model_distillation": _obj("Distill a teacher into a smaller student", "Train and evaluate distilled models"),
    },
    "09": {
        "01_mdp_example": _obj("Formalize decision problems as MDPs", "Define states, actions, rewards, and transitions"),
        "02_mdp_solving": _obj("Solve MDPs with value iteration or policy iteration", "Compute optimal value functions and policies"),
        "03_value_iteration": _obj("Implement value iteration and interpret convergence", "Apply to small grid-world or similar MDPs"),
        "01_q_learning": _obj("Implement Q-learning for model-free control", "Use exploration (e.g. ε-greedy) and tune hyperparameters"),
        "02_sarsa_algorithm": _obj("Implement SARSA and compare with Q-learning", "Understand on-policy vs off-policy"),
        "03_policy_gradient_basics": _obj("Implement a simple policy gradient method", "Use rewards and baseline to reduce variance"),
        "01_dqn_implementation": _obj("Implement DQN with experience replay and target network", "Train on simple RL environments"),
        "02_actor_critic": _obj("Implement actor–critic algorithms", "Combine policy and value learning"),
        "03_ppo_algorithm": _obj("Implement PPO or a simplified variant", "Train and stabilize policy optimization"),
        "01_exploration_strategies": _obj("Apply ε-greedy, UCB, and similar strategies", "Balance exploration and exploitation"),
        "02_balancing_exploration": _obj("Compare exploration strategies in RL", "Tune exploration for sample efficiency"),
        "03_adaptive_exploration_ucb": _obj("Use UCB and adaptive exploration", "Apply to bandits and simple MDPs"),
        "01_rl_applications": _obj("Apply RL to games, control, or recommendation", "Identify reward design and environment interfaces"),
        "02_game_playing_agent": _obj("Build a game-playing RL agent", "Train and evaluate in a game environment"),
        "03_resource_optimization": _obj("Use RL for resource allocation or scheduling", "Define state, action, and reward for the domain"),
    },
    "10": {
        "01_gan_architecture": _obj("Implement a GAN (generator and discriminator)", "Train GANs and interpret mode collapse / stability"),
        "02_conditional_gans": _obj("Build conditional GANs for class- or label-controlled generation", "Generate by class or attribute"),
        "01_generative_vs_discriminative": _obj("Compare generative and discriminative models", "Choose paradigm for generation vs classification"),
        "02_generative_model_comparison": _obj("Compare GANs, VAEs, and flow-based models", "Select models by quality, diversity, and use case"),
        "03_probabilistic_generative_models": _obj("Use latent variable models and log-likelihood", "Implement and evaluate probabilistic generators"),
        "03_stylegan_basics": _obj("Understand StyleGAN-style architecture and style control", "Generate and manipulate images with style"),
        "04_training_techniques_gradient_penalties": _obj("Apply gradient penalties, spectral norm, and stabilization", "Improve GAN training stability"),
        "01_vae_implementation": _obj("Implement a VAE and train on images", "Interpret latent space and reconstruct samples"),
        "02_vae_applications": _obj("Apply VAEs to images, latent editing, or downstream tasks", "Use encoder–decoder for representation learning"),
        "02_image_generation_advanced": _obj("Use advanced image generation (e.g. diffusion, StyleGAN)", "Compare quality and controllability"),
        "03_vae_advanced_topics": _obj("Use β-VAE, disentanglement, or hierarchical VAEs", "Analyze latent structure and metrics"),
        "01_generative_ai_ethics": _obj("Identify ethical risks of generative AI (deepfakes, bias)", "Apply guidelines and mitigation strategies"),
        "02_deepfake_detection": _obj("Implement or use deepfake detection methods", "Evaluate detection performance and limitations"),
        "03_future_trends_research": _obj("Summarize trends in generative AI and multimodal models", "Connect current tools to research directions"),
        "01_generative_ai_applications": _obj("Apply generative AI to images, text, or multimodal tasks", "Design and evaluate applications"),
        "03_music_generation": _obj("Use or adapt models for music generation", "Understand representation and evaluation challenges"),
    },
    "11": {
        "01_model_serving_api": _obj("Expose a model via REST or similar API", "Implement request handling and basic validation"),
        "02_model_packaging": _obj("Package models (e.g. pickle, SavedModel, ONNX)", "Version and load models in production"),
        "03_local_deployment_testing": _obj("Deploy and test models locally", "Run integration and sanity checks"),
        "01_flask_api_deployment": _obj("Serve models with Flask", "Handle routing, errors, and load"),
        "02_fastapi_deployment": _obj("Serve models with FastAPI", "Use async, validation, and docs"),
        "03_model_versioning": _obj("Version models and configs", "Roll back and A/B test deployments"),
        "01_cloud_deployment": _obj("Deploy models on a major cloud provider", "Use managed ML services or VMs"),
        "02_aws_sagemaker": _obj("Deploy and manage models on AWS SageMaker", "Use training and hosting APIs"),
        "03_azure_ml_deployment": _obj("Deploy models with Azure ML", "Use endpoints, monitoring, and scaling"),
        "04_gcp_vertex_ai": _obj("Deploy models with GCP Vertex AI", "Use pipelines and model registry"),
        "01_docker_deployment": _obj("Containerize models with Docker", "Build images and run containers"),
        "02_kubernetes_deployment": _obj("Deploy model containers on Kubernetes", "Use scaling and ingress"),
        "03_cloud_deployment_comparison": _obj("Compare cloud ML platforms and deployment options", "Choose stack by cost, scale, and lock-in"),
        "01_model_monitoring": _obj("Monitor latency, throughput, and errors", "Set up dashboards and alerts"),
        "02_retraining_pipeline": _obj("Automate retraining and model updates", "Use triggers, data versioning, and validation"),
        "03_alerting_incident_management": _obj("Set up alerting and incident response for ML systems", "Define SLOs and runbooks"),
    },
    "12": {
        "01_project_structure_template": _obj("Set up a clear project structure for capstone work", "Use templates for code, data, and docs"),
        "02_data_collection_preprocessing": _obj("Collect, clean, and preprocess project data", "Document sources and pipelines"),
        "03_model_development": _obj("Train and iterate on models for the capstone", "Track experiments and hyperparameters"),
        "04_model_evaluation": _obj("Evaluate models with relevant metrics", "Report results and failure modes"),
        "05_deployment_example": _obj("Deploy a capstone model (local or cloud)", "Document API and usage"),
        "06_project_documentation_template": _obj("Write project documentation and final report", "Use provided templates and structure"),
    },
}


def fix_objectives(nb_path: Path, rel: str, course: str) -> bool:
    stem = Path(rel).stem
    spec = OBJECTIVES.get(course, {}).get(stem)
    if not spec:
        return False
    try:
        with open(nb_path, encoding="utf-8") as f:
            nb = json.load(f)
    except json.JSONDecodeError:
        return False
    changed = False
    for c in nb["cells"]:
        if c.get("cell_type") != "markdown":
            continue
        lines = c.get("source", [])
        if not isinstance(lines, list):
            continue
        src = "".join(lines)
        if "Understand the key concepts of this topic" not in src:
            continue
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]
            if "- Understand the key concepts of this topic" in line:
                if new_lines and "By completing this notebook" not in new_lines[-1]:
                    new_lines.append("By completing this notebook, you will:\n")
                for s in spec:
                    new_lines.append(f"- {s}\n")
                i += 1
                while i < len(lines) and (
                    "- Apply the topic using Python code examples" in lines[i]
                    or "- Practice with small, realistic datasets or scenarios" in lines[i]
                ):
                    i += 1
                continue
            new_lines.append(line)
            i += 1
        if new_lines != lines:
            c["source"] = new_lines
            changed = True
        break
    if changed:
        with open(nb_path, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
    return changed


def main():
    courses = sys.argv[1:] if len(sys.argv) > 1 else ["01", "02", "08", "09", "10", "11", "12"]
    for c in courses:
        num = c.zfill(2) if len(c) <= 2 else c
        folder = ROOT / f"Course {num}"
        if not folder.is_dir():
            print(f"Skip Course {num}")
            continue
        done = []
        for nb_path in sorted(folder.rglob("*.ipynb")):
            rel = nb_path.relative_to(folder).as_posix()
            if "DOCS" in rel or "PROJECTS" in rel or ".ipynb_checkpoints" in rel:
                continue
            if fix_objectives(nb_path, rel, num):
                done.append(rel)
        print(f"[Course {num}] Updated objectives: {len(done)}")
        for r in done:
            print(" ", r)
        print()


if __name__ == "__main__":
    main()
