# Related Repositories

This page explains how the control repositories fit together.

## Public Control Family

| Repo | Role | Why it matters |
|---|---|---|
| [`robotics-control-learning-labs`](https://github.com/WikiGenius/robotics-control-learning-labs) | Public control hub | Organizes state-space, LQR, observers, and reproducible control labs. |
| [`ipendulum`](https://github.com/WikiGenius/ipendulum) | Inverted-pendulum control lab | Shows applied MATLAB/Simulink control on a classic benchmark: PID, LQR, pole placement, observers, LQG, and animations. |
| [`wmm-trajectory-tracking`](https://github.com/WikiGenius/wmm-trajectory-tracking) | Whole-body trajectory tracking | Connects control to mobile-manipulator motion and scan execution. |
| [`Cruise_control`](https://github.com/WikiGenius/Cruise_control) | MATLAB/Simulink control exercise | Shows classical control modeling and simulation practice. |
| [`RoboticScrewTheoryToolkit`](https://github.com/WikiGenius/RoboticScrewTheoryToolkit) | Robot math toolkit | Supports kinematics, Jacobians, screw theory, and manipulator modeling. |

## Archived Control History

| Repo | Status | Note |
|---|---|---|
| [`3dof-robot-arm-report`](https://github.com/WikiGenius/3dof-robot-arm-report) | Archived | Preserved as an older robot-arm modeling/control report, but no longer part of the active public portfolio. |

## Private Companion Layer

Unpublished control experiments, parameter sweeps, paper-specific uncertainty-aware control code, advisor notes, and internal ablations should remain private.

When a private experiment becomes safe to show publicly, release only a distilled version:

1. Use synthetic or non-sensitive data.
2. Remove unpublished algorithm details that belong in a paper first.
3. Include a short model derivation or citation.
4. Add reproducible commands.
5. Add plots under `results/` and figures or GIFs under `media/`.
6. State what was simplified.

## Connection to Main Research

The control family supports structure-aware mobile manipulation by providing:

- stable base-arm trajectory tracking,
- LQR/observer baselines for comparison,
- state-space modeling practice,
- kinematic foundations for arm motion,
- experiment logs and metrics that can later connect to active scanning.

The downstream public demo is [`line-scan-mobile-manipulator-demo`](https://github.com/WikiGenius/line-scan-mobile-manipulator-demo). That repo should eventually consume simplified controllers or metrics from this control family.

## Pinning Note

Keep [`robotics-control-learning-labs`](https://github.com/WikiGenius/robotics-control-learning-labs) pinned as the broad control hub. `ipendulum` is a strong public support repo under that hub, but it does not need to replace one of the six pins unless the pinning strategy changes later.
