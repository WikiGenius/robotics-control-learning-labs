# Robotics Control Learning Labs

An index of control and robot-geometry projects supporting [perception-aware motion planning](https://github.com/WikiGenius). This repository is a navigation hub; it does not currently contain a runnable lab.

## Where to start

| Project | Study or implementation | Research connection |
| --- | --- | --- |
| [iPendulum](https://github.com/WikiGenius/ipendulum) | PID, LQR/LQG, observers, and simulation demonstrations | Feedback and estimation foundations |
| [WMM planning and tracking](https://github.com/WikiGenius/wmm-planning-and-tracking) | Differential-drive mobile-manipulator planning and torque-level tracking | Coordinated motion execution |
| [Cruise Control](https://github.com/WikiGenius/Cruise_control) | Motor/control and energy analysis in MATLAB/Simulink | Motion effort and actuator behavior |
| [Screw Theory Toolkit](https://github.com/WikiGenius/RoboticScrewTheoryToolkit) | Kinematics, Jacobians, and inverse kinematics | Feasibility of robot and sensor poses |

## Why control matters for perception-aware planning

A sensing plan is useful only if the robot can execute it accurately enough for the task. Tracking error, actuator limits, and motion cost can affect observation quality. These projects provide foundations for studying that connection; they do not yet implement a common perception-aware controller.

The broader research is adaptable to different sensors and robot platforms. The cart-pole and wheeled-manipulator models are specific examples.

## Planned additions

Add a self-contained lab only when its code, dependencies, run command, and expected outputs are available. Useful future comparisons include tracking accuracy, control effort, and sensitivity to disturbances.

Run instructions and license terms belong to each linked project. MATLAB/Simulink examples may require licensed toolboxes. No project-wide open-source license is granted by this index.
