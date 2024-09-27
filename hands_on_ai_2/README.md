### **Assignment 1 - Recap of Hands-On AI I**

#### Overview
This assignment serves as a recap of core concepts from **Hands-On AI I**, with a focus on practical machine learning techniques, including **logistic regression**, **neural networks**, and data processing. The assignment ensures a solid understanding of foundational AI concepts and prepares for more advanced topics.

#### Key Tasks
- **Logistic Regression**: Reviewed the implementation of logistic regression, focusing on gradient-based optimization for binary classification tasks. Explored the impact of regularization techniques on overfitting and model performance.
- **Neural Networks**: Revisited the construction and training of neural networks using backpropagation. Focused on how different architectures affect convergence and classification accuracy.
- **Data Handling**: Processed and split datasets into training, validation, and test sets, implementing methods to ensure data integrity and consistency for model evaluation.
- **Model Comparison**: Compared logistic regression and neural network performance on various datasets, assessing their strengths and weaknesses in terms of convergence speed and accuracy.

---

### **Assignment 2 - The Vanishing Gradient Problem**

#### Overview
This assignment addresses the **vanishing gradient problem**, a fundamental challenge in training deep neural networks. It explores how activation functions and initialization techniques impact gradient propagation and how these issues can be mitigated in deeper networks.

#### Key Tasks
- **Gradient Flow Analysis**: Investigated how gradients diminish as they are propagated through the layers of a deep neural network, leading to slower learning or stagnation. Visualized gradient magnitudes across layers to diagnose the problem.
- **Activation Function Comparison**: Tested different activation functions, including **sigmoid**, **tanh**, and **ReLU**, to analyze their impact on gradient flow and model performance. Demonstrated why **ReLU** and its variants are preferred in deep learning.
- **Weight Initialization**: Explored how different initialization schemes (e.g., **Xavier initialization**) affect gradient flow and convergence in deep networks.
- **Model Optimization**: Applied techniques like **batch normalization** and **layer normalization** to improve gradient stability and model convergence, demonstrating a reduction in training time and improved accuracy.

---

### **Assignment 3 - Recurrent Neural Networks (RNNs)**

#### Overview
This assignment focuses on **Recurrent Neural Networks (RNNs)** and their ability to handle sequential data, such as time-series analysis and natural language processing. The project emphasizes the training of RNNs, backpropagation through time (BPTT), and the challenges of long-term dependencies in sequences.

#### Key Tasks
- **RNN Implementation**: Built a simple RNN using **PyTorch**, implementing forward and backward passes across sequences to capture temporal dependencies. Addressed challenges related to gradient flow across time steps.
- **Backpropagation Through Time (BPTT)**: Implemented BPTT to compute gradients over multiple time steps, ensuring that the model could learn from past data in a sequence.
- **Time-Series Prediction**: Trained the RNN on a time-series dataset, focusing on predicting future values based on historical patterns. Evaluated model performance using accuracy and mean squared error.
- **Long-Term Dependency Challenge**: Analyzed the difficulty of learning long-term dependencies in RNNs and explored how vanishing gradients impact learning in long sequences.

---

### **Assignment 4 - Introduction to Reinforcement Learning**

#### Overview
This assignment introduces the fundamentals of **Reinforcement Learning (RL)** using the **FrozenLake** environment from OpenAI Gym. The task involves navigating an agent through a frozen lake while avoiding holes, using a variety of RL techniques to maximize the cumulative reward.

#### Key Tasks
- **Environment Exploration**: Explored the **FrozenLake** environment, analyzing the types of surfaces and potential hazards (e.g., holes, frozen surfaces, and the goal location).
- **Policy Development**: Developed a policy for navigating the lake by balancing exploration and exploitation strategies.
- **Q-Learning Implementation**: Implemented **Q-learning**, a model-free RL algorithm, to learn the optimal policy by maximizing the agent’s cumulative reward over time.
- **Value Iteration**: Applied **value iteration** to compute the optimal value function and derived the optimal policy for the agent.
- **Policy Evaluation**: Evaluated the learned policies by simulating the agent’s behavior over multiple episodes, measuring success rates, and analyzing the agent’s ability to reach the goal.

---

### **Assignment 5 - Drug Discovery**

#### Overview
This assignment applies AI techniques to **drug discovery**, focusing on molecular property prediction and optimization. The project utilizes deep learning models to predict chemical properties based on molecular structure, simulating real-world applications in pharmaceutical research.

#### Key Tasks
- **Molecular Data Handling**: Processed molecular datasets, preparing data for training by normalizing features and converting chemical properties into a format suitable for deep learning models.
- **Neural Network Design**: Built and trained a **fully connected neural network** using **PyTorch** to predict molecular properties. The model was optimized for accuracy in classifying molecules based on their chemical structure.
- **Model Evaluation**: Assessed model performance using precision, recall, and F1-score, focusing on how well the network predicted key properties relevant to drug discovery.
- **Optimization Techniques**: Tuned hyperparameters such as learning rate, batch size, and the number of layers to improve model accuracy. Explored how different architectures impacted the ability of the network to generalize to unseen chemical data.

---

### **Assignment 6 - Language Modeling with LSTM Networks**

#### Overview
This assignment focuses on **Long Short-Term Memory (LSTM)** networks, a type of RNN designed to handle long-range dependencies in sequential data. The project applies LSTM networks to language modeling tasks, focusing on text generation and sequence prediction.

#### Key Tasks
- **LSTM Implementation**: Built an LSTM network using **PyTorch**, training it on sequential text data to model and predict word sequences. Implemented backpropagation through time to handle long sequences.
- **Data Preparation**: Processed text data for language modeling, tokenizing sequences and converting them into numerical representations for input into the LSTM model.
- **Text Generation**: Trained the LSTM on a large corpus of text data, generating new text sequences by sampling from the learned probability distributions. Demonstrated the network’s ability to generate coherent text based on learned patterns.
- **Model Evaluation**: Assessed model performance using perplexity and cross-entropy loss, evaluating the LSTM's ability to predict and generate text with long-term dependencies.

---
