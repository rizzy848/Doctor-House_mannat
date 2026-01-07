# Doctor House - AI Medical Diagnosis System

An intelligent symptom-based disease diagnosis system that uses **graph algorithms** and **probability calculations** to predict potential diseases based on patient symptoms. Built with Python and featuring an intuitive GUI for remote medical consultation.

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)](https://docs.python.org/3/library/tkinter.html)
[![Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-orange.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🏥 Project Overview

Doctor House is a diagnostic support tool that helps identify potential diseases based on a combination of symptoms reported by patients. Using a graph-based approach and weighted symptom analysis, the system calculates disease probabilities and provides medical advice and precautions.

**Key Features:**
- 🔍 **Symptom-Based Diagnosis** - Input symptoms to receive potential disease predictions
- 📊 **Probability Visualization** - Interactive bar charts showing disease likelihood percentages
- 💡 **Medical Guidance** - Detailed disease descriptions and precautionary measures
- 🎯 **Smart Search** - Autocomplete dropdown for easy symptom selection
- 📈 **Graph Algorithm** - Shortest path algorithms for symptom-disease correlation
- 🖥️ **User-Friendly Interface** - Clean, modern GUI with fullscreen support

## 🧠 Algorithm & Architecture

### Graph-Based Disease Model

The system uses a **bipartite graph structure** where:
- **Symptom vertices** represent medical symptoms (e.g., headache, fever)
- **Disease vertices** represent medical conditions (e.g., flu, malaria)
- **Weighted edges** connect symptoms to diseases based on severity scores

### Diagnosis Algorithm

```python
1. User selects multiple symptoms
2. System finds shortest paths between symptom pairs
3. Calculates path scores using edge weights (severity)
4. Aggregates scores for each disease along paths
5. Converts scores to probabilities (normalized percentages)
6. Returns top disease candidates with confidence levels
```

**Mathematical Foundation:**
- **Edge Weight**: `w = 1 / severity_score` (inverse relationship)
- **Path Score**: Sum of edge weights along the path
- **Disease Score**: Aggregated path scores passing through disease vertex
- **Probability**: `P(disease) = (1/score) / Σ(1/all_scores) × 100%`

### Architecture Diagram

```
┌─────────────────────────────────────────────┐
│            Presentation Layer               │
│         (main.py - Tkinter GUI)             │
├─────────────────────────────────────────────┤
│            Business Logic Layer             │
│      (backend.py - Graph Algorithms)        │
├─────────────────────────────────────────────┤
│              Data Layer                     │
│   (CSV Files - Disease/Symptom Database)    │
└─────────────────────────────────────────────┘
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.13** or higher
- **pip** package manager
- Required packages listed in `requirements.txt`

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/doctor-house.git
cd doctor-house
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python main.py
```

## 📖 How to Use

### Basic Workflow

1. **Launch Application**
   - Run `python main.py`
   - Application opens in fullscreen mode (press ESC to toggle)

2. **Select Symptoms**
   - Type in the search bar to find symptoms
   - Click on symptoms from dropdown to add them to your selection
   - Selected symptoms appear in the right panel

3. **Get Diagnosis**
   - Click **"Check Diagnosis"** button
   - View probability bar chart showing potential diseases
   - Click on disease names to see detailed descriptions and advice

4. **Review Medical Information**
   - Read disease descriptions
   - Review precautionary measures
   - Use information for preliminary assessment

### Example Scenario

```
Selected Symptoms:
  - High fever
  - Headache
  - Nausea
  - Fatigue

Results:
  - Malaria: 45%
  - Typhoid: 30%
  - Dengue: 25%
```

## 📊 Data Structure

### Graph Representation

```python
class Graph:
    """
    Bipartite graph with symptoms and diseases as vertices
    - Vertices: {symptom_name or disease_name}
    - Edges: weighted connections (symptom ↔ disease)
    - Edge Weight: 1 / severity_score
    """
```

### Disease Class

```python
class Disease:
    """
    Represents a medical condition
    - name: str - Disease identifier
    - symptoms: set - Associated symptoms
    - description: str - Medical description
    - advice: list - Precautionary measures
    """
```

## 📁 Project Structure

```
doctor-house/
├── main.py                      # GUI application (Tkinter)
├── backend.py                   # Core logic (Graph algorithms)
├── requirements.txt             # Python dependencies
├── Symptom-severity.csv         # Symptom severity weights (1-7 scale)
├── dataset.csv                  # Disease-symptom relationships
├── symptom_Description.csv      # Disease descriptions
├── symptom_precaution.csv       # Medical advice/precautions
└── README.md                    # This file
```

## 🔑 Key Technical Highlights

### Data Structures & Algorithms
- ✅ **Graph Theory** - Bipartite graph implementation
- ✅ **Shortest Path Algorithm** - BFS-based pathfinding
- ✅ **Probability Theory** - Bayesian-inspired score normalization
- ✅ **Object-Oriented Design** - Clean class hierarchies

### Software Engineering Practices
- ✅ **Separation of Concerns** - Backend logic separated from GUI
- ✅ **Type Hints** - Full type annotations for better code quality
- ✅ **Documentation** - Comprehensive docstrings and comments
- ✅ **Error Handling** - Graceful handling of edge cases
- ✅ **Code Quality** - PEP 8 compliant, python-ta verified

### Python Skills Demonstrated
- 🐍 Advanced data structures (graphs, custom classes)
- 🐍 GUI development (Tkinter)
- 🐍 Data visualization (Matplotlib)
- 🐍 File I/O and CSV processing
- 🐍 Event-driven programming
- 🐍 Algorithm implementation (BFS, shortest path)

## 📈 Algorithm Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Load Graph | O(D × S) | O(D + S + E) |
| Add Vertex | O(1) | O(1) |
| Add Edge | O(1) | O(1) |
| Shortest Path (BFS) | O(V + E) | O(V) |
| Calculate Diagnosis | O(n² × (V + E)) | O(V) |

**Where:**
- D = Number of diseases (~41)
- S = Number of symptoms (~133)
- E = Number of edges (disease-symptom connections)
- V = Total vertices (D + S)
- n = Number of input symptoms

## 🎨 GUI Features

### Main Window
- **Search Bar** - Type-ahead symptom search
- **Dropdown Menu** - Filtered symptom suggestions
- **Selected Symptoms List** - View chosen symptoms
- **Clear Button** - Reset selection
- **Diagnose Button** - Calculate and display results

### Diagnosis Window
- **Bar Chart** - Visual probability distribution
- **Disease Buttons** - Interactive disease selection
- **Information Panel** - Scrollable disease details and advice
- **Fullscreen Toggle** - ESC key for better viewing

### Styling
- **Modern Theme** - Clean, professional color scheme
- **Custom Fonts** - Lexend font family for readability
- **Responsive Layout** - Dynamic resizing with tkinter grid/pack
- **Color Palette**:
  - Background: `#ADB2D4` (soft blue-gray)
  - UI Elements: `#2b2b2b` (dark)
  - Accents: `#FFF2F2` (light pink)

## 📚 Dataset Information

### Symptom Severity Database
- **133 unique symptoms** with severity weights (1-7 scale)
- Higher weights indicate more serious symptoms
- Used to calculate edge weights in the graph

### Disease Database
- **41 different diseases** across multiple categories
- Infectious diseases (Malaria, Dengue, Tuberculosis)
- Chronic conditions (Diabetes, Hypertension, Arthritis)
- Liver diseases (Hepatitis A-E, Jaundice)
- Comprehensive symptom associations

### Medical Advice Database
- **Disease descriptions** - Medical explanations
- **Precautionary measures** - 4 recommendations per disease
- **Treatment guidance** - First-aid and consultation advice

## ⚠️ Disclaimer

**Important Medical Notice:**

This application is designed for **educational and informational purposes only**. It is NOT a substitute for professional medical advice, diagnosis, or treatment.

- 🏥 Always consult a qualified healthcare provider for medical concerns
- 🚫 Do not rely solely on this tool for medical decisions
- ⚕️ In case of emergency, contact emergency services immediately
- 📋 Results are probabilistic estimates, not definitive diagnoses

## 🧪 Testing

The codebase includes comprehensive testing support:

```bash
# Run python-ta code quality checks
python -m python_ta backend.py
python -m python_ta main.py

# Check code style
python -m pylint backend.py main.py
```

## 🛠️ Future Enhancements

- [ ] **Machine Learning Integration** - Train ML models on symptom patterns
- [ ] **User History** - Save and track patient symptom history
- [ ] **Multi-language Support** - Internationalization for global use
- [ ] **Doctor Consultation** - Integration with telemedicine platforms
- [ ] **Mobile App** - Cross-platform mobile application
- [ ] **Expanded Database** - More diseases and symptoms
- [ ] **Severity Analysis** - Track symptom progression over time
- [ ] **Export Reports** - Generate PDF diagnosis reports

## 👥 Team

**Project developed for CSC111 - Foundations of Computer Science**
- University of Toronto
- Winter 2024-2025 Term

## 🎓 Acknowledgments

- **Python Libraries**: Tkinter, Matplotlib, python-ta
- **Data Sources**: Medical symptom and disease databases (educational use)
- **Course Staff**: University of Toronto CSC111 instructors and TAs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

This is an academic project. If you'd like to use or extend this code:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

For questions or feedback about this project, please open an issue on GitHub.

---

**Note:** This is an educational project demonstrating graph algorithms, data structures, and GUI development. All medical information is sourced from public datasets and should not be used for actual medical diagnosis.
