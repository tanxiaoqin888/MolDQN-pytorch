import torch

atom_types=['C', 'O', 'N']
max_steps_per_episode=40
allow_removal=True
allow_no_modification=True
allow_bonds_between_rings=False
allowed_ring_sizes=[3, 4, 5, 6]
replay_buffer_size=1000000
learning_rate=1e-4
learning_rate_decay_steps=10000
learning_rate_decay_rate=0.8
num_episodes=5000
batch_size=64
learning_frequency=4
update_frequency=20
grad_clipping=10.0
gamma=0.9
double_q=True
num_bootstrap_heads=12
prioritized=False
prioritized_alpha=0.6
prioritized_beta=0.4
prioritized_epsilon=1e-6
fingerprint_radius=3
fingerprint_length=2048
dense_layers=[1024, 512, 128, 32]
activation='relu'
optimizer='Adam'
batch_norm=False
save_frequency=1000
max_num_checkpoints=100
discount_factor=0.7
device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')
