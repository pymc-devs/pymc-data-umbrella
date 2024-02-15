import autograd.numpy as np
from minimc import neg_log_mvnormal, mixture
from minimc.autograd_interface import AutogradPotential
from minimc.integrators_slow import leapfrog as leapfrog_slow
import scipy.stats as st
import matplotlib.pyplot as plt
from tqdm import tqdm

mu1 = np.ones(2)
cov1 = 0.5 * np.array([[1.0, 0.7], [0.7, 1.0]])
mu2 = -np.ones(2)
cov2 = 0.2 * np.array([[1.0, -0.6], [-0.6, 1.0]])
neg_log_p = mixture(
    [
neg_log_mvnormal(mu1, cov1),
neg_log_mvnormal(mu2, cov2),
    ],
    [0.3, 0.3],
)
np.random.seed(16)
momenta = st.norm(0, 1).rvs(size=(5, 2))
n = 5
initial_positions = st.norm(0, 0.1).rvs(size=(n, 2))

all_positions = []
for initial_position in tqdm(initial_positions):
    potential = AutogradPotential(neg_log_p)
    negative_log_prob = lambda q: potential(q)[0]  # NOQA
    dVdq = lambda q: potential(q)[1]  # NOQA

    # collect all our samples in a list
    samples = [initial_position]
    positions = []
    for p0 in tqdm(momenta):
        # Integrate over our path to get a new position and momentum
        q_new, p_new, path, momentums, _ = leapfrog_slow(
            samples[-1], p0, dVdq, path_len=10, step_size=0.01
        )
        positions.append(path)
        samples.append(q_new)
    all_positions.append(np.array(positions))

fig, ax = plt.subplots(
    figsize=np.array([1468, 720]) / plt.rcParams["figure.dpi"], constrained_layout=True
)

idxs = [4, 3, 2, 1, 0]

colors = ["#8dbcc7", "#4c8f9e", "#365359", "#84aab3", "#0d5e70"] #blues
for idx in idxs:
    positions = (all_positions[idx])*(-2.05)
    ax.plot(*positions[3].T, "-", lw=6, color=colors[idx], alpha=0.5)
    ax.plot(*positions[3, -1], "o", ms=10, color=colors[idx], mfc="#ffffff", mew=4,alpha=0.5)


idxs = [0, 1, 2, 3, 4]
colors = ["#857f82", "#5e5c5c", "#a3a2a2", "#333132", "#1f1c1d"] #blacks
for idx in idxs:
    positions = (all_positions[idx])*(-1.09)-1.00
    ax.plot(*positions[3].T, "-", lw=4, color=colors[idx], alpha=0.5)
    ax.plot(*positions[3, -1], "o", ms=10, color=colors[idx], mfc="#ffffff", mew=4,alpha=0.5)

fig.set_facecolor("#ffffff")
ax.set_axis_off()

fig.savefig("banner.png", pad_inches=1.0, transparent=True)





