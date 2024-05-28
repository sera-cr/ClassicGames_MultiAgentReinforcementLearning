from pettingzoo.classic import connect_four_v3

env = connect_four_v3.env(render_mode="human")
env.reset(seed=42)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
    else:
        mask = observation["action_mask"]
        print(mask)
        # print(env.unwrapped.board)
        # this is where you would insert your policy
        prueba = {}
        prueba['12234'] = {0: 0.1, 1: 0.1, 2: 0.1, 3: 0.1, 4: 0.1, 5: 0.1, 6: 0.1, 7: 0.1, 8: 0.1}
        action = env.action_space(agent).sample(mask)

    env.step(action)
env.close()