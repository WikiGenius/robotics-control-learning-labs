# Robotics Control Learning Labs

## Purpose

This repository is a public control-foundation hub for organizing robotics/control learning artifacts, including state-space modeling, LQR, observers, trajectory tracking, and MATLAB/Simulink workflows.

It supports the broader robotics research portfolio without exposing unpublished PhD control experiments, advisor notes, paper drafts, or private ablations.

## Relation to Robotics and Control Research

My research direction requires planning and control for mobile manipulation under sensing, geometry, and uncertainty constraints. This repo supports that direction by organizing:

- state-space modeling practice,
- LQR and feedback-control baselines,
- observer/state-estimation examples,
- trajectory-tracking foundations,
- MATLAB/Simulink and Python analysis patterns,
- public control examples that can later connect to active scanning.

Related public repos:

| Related repo | Public role |
|---|---|
| [`ipendulum`](https://github.com/WikiGenius/ipendulum) | Inverted-pendulum MATLAB/Simulink lab with PID, LQR, pole placement, observers, LQG, and demo animations. |
| [`wmm-trajectory-tracking`](https://github.com/WikiGenius/wmm-trajectory-tracking) | Whole-body mobile-manipulator trajectory tracking and control support. |
| [`Cruise_control`](https://github.com/WikiGenius/Cruise_control) | MATLAB/Simulink control exercise and energy/control artifact. |
| [`RoboticScrewTheoryToolkit`](https://github.com/WikiGenius/RoboticScrewTheoryToolkit) | Kinematics, screw theory, Jacobians, and robot math foundations. |
| [`line-scan-mobile-manipulator-demo`](https://github.com/WikiGenius/line-scan-mobile-manipulator-demo) | Downstream active-scanning scaffold that will need planning/control foundations. |

## Maturity Level

**Current status:** Public research organization repo / control-family hub.

This repository currently organizes the public-facing control structure and connects related control repos. It does not currently contain a runnable in-repo lab script, complete control library, or tested robot controller.

## Implemented Now

- [x] Repository structure.
- [x] README and project organization.
- [x] Public related-repository map.
- [x] Link to public inverted-pendulum control support repo.
- [x] Link to mobile-manipulator trajectory-tracking support repo.
- [ ] In-repo public-safe LQR lab.
- [ ] Observer lab in this repo.
- [ ] MATLAB/Simulink lab collection in this repo.
- [ ] Mobile-manipulator tracking comparison.
- [ ] Paper-supporting implementation.

## Current Runnable Artifact

There is currently no runnable in-repo lab script in this public hub.

For concrete public control examples, see [`ipendulum`](https://github.com/WikiGenius/ipendulum) and the related repositories listed above.

## Planned Labs

- Public-safe LQR lab.
- Observer/state-estimation lab.
- State-space modeling notes.
- MATLAB/Simulink control examples.
- Trajectory-tracking metric comparison.
- Public plot or GIF generated from a real lab.

## Limitations

This repository is currently an early-stage public control scaffold. It does not yet include:

- a full control curriculum,
- a tested robot controller,
- a mobile-manipulator tracking benchmark,
- complete observer labs,
- paper-level results.

MATLAB/Simulink examples may require licensed toolboxes.

## How to Run

No run command is available yet because no in-repo runnable lab script is currently included.

When the first real public-safe lab is added and tested, this section should include:

```bash
python scripts/<lab_name>.py
```

Do not add generated plots or commands until the script and outputs actually exist.

## Rights and Reuse

This repository is shared as a public academic portfolio/scaffold. Unless a separate open-source license is explicitly added, all rights are reserved by the author.

## Related Organization

See [`docs/related-repositories.md`](docs/related-repositories.md) for how the control repositories fit into the public/private research structure.
