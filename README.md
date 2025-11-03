# Dinkinesh-Selam_formation

Additional supporting information. Bern SPH simulation data for Raducan et al., Multiple moonlet mergers as the origin of the Dinkinesh-Selam system (Nature Communications).

This repository provides the deposited simulation data and analysis scripts used in the publication. It includes results from Bern SPH, REBOUND, and HIDRORINGS simulations, along with asteroid boulder size–frequency distribution (SFD) data and plotting scripts.

## Repository Layout

Dinkinesh-Selam_formation/
├── README.txt                         # Repository overview and documentation
│
├── SPH_simulations/                   # Bern SPH data and analysis scripts
│   │
│   ├── Dimorphos/                     # SPH simulations for Dimorphos formation
│   │   ├── parameters/                # Input parameters (impact angle, velocity)
│   │   ├── shape_10/                  # SPH input files (10 vol% boulders: shape, EOS, strength/friction, porosity)
│   │   ├── shape_15/                  # SPH input files (15 vol% boulders: shape, EOS, strength/friction, porosity)
│   │   ├── shape_20/                  # SPH input files (20 vol% boulders: shape, EOS, strength/friction, porosity)
│   │   └── Simulations_summary.pdf    # Summary of simulation runs and Dimorphos results
│   │
│   └── Selam/                         # SPH simulations for Selam formation
│       ├── README.txt                 # Details of Selam SPH runs
│       ├── parameters/                # Input parameters (impact angle, velocity)
│       ├── shape_love_high/           # SPH input files & shape model (outer lobe)
│       ├── shape_peace_high/          # SPH input files & shape model (inner lobe)
│       └── Plots/                     # Python scripts used to generate the figures in the paper
│
├── HIDRORINGS_simulations/            # HIDRORINGS hydrodynamics simulation data
│   ├── README.txt                     # Details of HIDRORINGS data and setup
│   ├── fig3.py                        # Script to reproduce HIDRORINGS figure (Fig. 3)
│   └── sup3.txt                       # Supplementary data for HIDRORINGS runs
│
└── REBOUND_simulations/               # REBOUND N-body simulation data
    ├── coll_log.txt                   # REBOUND simulation output (v/v_esc, d/R_primary, m_lobe/M_primary)
    └── rebound_collisions.py          # Python script to reproduce Fig. 6

---

## Citation

If you use this repository or its data, please cite:

> Raducan, S. *et al.* (2025). *Multiple moonlet mergers as the origin of the Dinkinesh–Selam system.* Nature Communications.

Data and code: **Dinkinesh-Selam_formation** repository.

---

## Contact

For questions regarding SPH, REBOUND, or HIDRORINGS datasets, please contact the corresponding author listed in the publication.
