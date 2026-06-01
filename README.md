# Robotics Control Learning Labs

## Overview
This repository is a public learning-lab scaffold for robotics and control simulations. It is intended to collect reproducible examples for state-space modeling, feedback control, observers, LQR design, and MATLAB/Simulink experiments.

The current repository is a documentation-first scaffold. Labs, scripts, reports, and result figures will be added incrementally.

## Research/Engineering Motivation
Control theory is one of the foundations of robotics. Mobile robots, manipulators, drones, and autonomous systems all rely on models, feedback, state estimation, and stability-aware design.

This repository is meant to make control experiments easier to revisit, reproduce, and explain: each lab should connect a model, a controller, simulation results, and a short engineering interpretation.

## Features
- Planned reproducible labs for state-space modeling.
- Planned LQR and feedback-controller examples.
- Planned observer/state-estimation simulations.
- Planned MATLAB/Simulink and optional Python analysis workflows.
- Folder structure for reports, experiment logs, media, and results.

## Method
Each lab will follow a repeatable structure:

1. Define the physical or mathematical model.
2. Derive or document the state-space representation.
3. Design a controller or observer.
4. Simulate the closed-loop behavior.
5. Plot key signals such as state, control effort, tracking error, and energy use.
6. Record limitations and lessons learned.

The repository will prioritize clear, reproducible educational examples over unpublished or overly specialized experiment details.

## Installation
Clone the repository:

```bash
git clone https://github.com/WikiGenius/robotics-control-learning-labs.git
cd robotics-control-learning-labs
```

Optional Python environment for analysis scripts:

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

MATLAB/Simulink labs will list their required toolboxes in the lab notes.

## Run
This repository currently contains the public structure. Planned run patterns:

```bash
python scripts/<lab_name>.py
```

For MATLAB/Simulink labs, open the relevant `.m`, `.mlx`, or `.slx` file and run from MATLAB after checking the lab-specific documentation.

## Results
Results will be stored in `results/`, with figures or videos in `media/`.

Planned artifacts:

- Step responses and tracking plots.
- Control effort and energy summaries.
- Observer convergence plots.
- Simulink block-diagram screenshots.

## Limitations
- The repository is currently a scaffold; complete labs are not yet included.
- MATLAB/Simulink examples may require licensed toolboxes.
- Public labs will be simplified for clarity and reproducibility.

## Roadmap
- [ ] Add first state-space modeling lab.
- [ ] Add LQR baseline controller.
- [ ] Add observer design example.
- [ ] Add metrics and experiment logs.
- [ ] Add paper/report links where relevant.

## Citation / Acknowledgment
Acknowledge any textbook, course, paper, MATLAB example, Python library, or robotics/control framework used in each lab. Third-party materials remain under their own licenses.
