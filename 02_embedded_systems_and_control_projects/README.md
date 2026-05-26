# Embedded Systems and Control Projects

This folder shows the EEE engineering base behind the biomedical AI work.

## Included Themes

- Microcontroller-based aquaculture monitoring for catfish/tilapia fisheries.
- PID control and control-system analysis.
- Digital filter design.
- Power electronics / multilevel inverter work.
- Project showcasing awards and engineering competition evidence.

## Portfolio Positioning

These projects should be framed as applied engineering foundations:

- Sensors and microcontrollers for real-world monitoring.
- Feedback control for electromechanical systems.
- Signal filtering and analysis.
- Embedded systems thinking that transfers naturally into biomedical device development.

## Suggested README Structure for Each Project

When splitting into individual public repos later, use:

- Problem statement.
- Hardware/software stack.
- Circuit or system architecture.
- Control/signal-processing method.
- Evaluation criteria.
- Limitations and future work.

Useful math framing for PID work:

```latex
u(t)=K_p e(t)+K_i\int_0^t e(\tau)d\tau+K_d\frac{de(t)}{dt}
```

Useful framing for filtering:

```latex
y[n]=\sum_{k=0}^{M} b_k x[n-k]-\sum_{k=1}^{N} a_k y[n-k]
```

