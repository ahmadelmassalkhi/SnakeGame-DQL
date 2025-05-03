from stable_baselines3 import DQN
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.monitor import Monitor
from gymnasium.wrappers import FlattenObservation, TimeLimit
from SnakeEnv import SnakeEnv

if __name__ == "__main__":
    dir = "./DQN"

    # env = SnakeEnv()
    env = SnakeEnv(render_mode="human")
    env = TimeLimit(FlattenObservation(Monitor(env)), max_episode_steps=200)
    eval_callback = EvalCallback(
        env,
        best_model_save_path=dir+"/best_model",
        log_path=dir+"/logs",
        eval_freq=5000,
        deterministic=True,
        render=False  # Disable rendering during evaluation for better performance
    )

    model = DQN(
        "MlpPolicy",
        env,
        verbose=1,
        learning_rate=1e-3,  # Higher learning rate for faster convergence
        buffer_size=100_000,  # Smaller buffer size to fit the environment complexity
        batch_size=64,  # Smaller batch size for stability
        train_freq=4,  # Train every 4 steps
        gradient_steps=1,
        target_update_interval=1000,  # Update target network less frequently
        device="cuda",
        exploration_initial_eps=1.0,
        exploration_final_eps=0.1,  # Lower final epsilon for better exploitation
        exploration_fraction=0.2,  # Longer exploration phase
        gamma=0.99,  # Higher discount factor for long-term rewards
        tau=1.0,  # Soft update coefficient
    )

    model.learn(total_timesteps=100_000, callback=eval_callback)  # Increased timesteps for better training
    model.save(dir+"/snake_dqn")
