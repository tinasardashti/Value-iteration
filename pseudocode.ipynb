{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "b2539c92-58f8-498e-b69b-1d4071930675",
   "metadata": {},
   "source": [
    "# Algorithm & Pseudocode Comparison\n",
    "\n",
    "This section presents the Value Iteration algorithm implemented in this project and explains how it relates to the classical version described in *Artificial Intelligence: Foundations and Computational Agents* (Poole and Mackworth, Figure 9.16)."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f59912ee-50fb-4ea3-b5fc-a4a0b0bc41c7",
   "metadata": {},
   "source": [
    "## 1. Original Textbook Pseudocode (Figure 9.16)\n",
    "\n",
    "The standard Value Iteration algorithm is defined as a synchronous update process, where a new value function is computed entirely from the previous iteration."
   ]
  },
  {
   "cell_type": "raw",
   "id": "83d8b0cf-7a42-41d3-8b17-ac437694810c",
   "metadata": {},
   "source": [
    "procedure ValueIteration(S, A, P, R, γ)\n",
    "\n",
    "    initialize V₀[s] arbitrarily for all s in S\n",
    "    k = 0\n",
    "\n",
    "    repeat:\n",
    "        k = k + 1\n",
    "\n",
    "        for each state s in S:\n",
    "            Vₖ[s] = max over actions a of:\n",
    "                     R(s, a) + γ * sum over s' of P(s' | s, a) * Vₖ₋₁[s']\n",
    "\n",
    "    until convergence\n",
    "\n",
    "    for each state s in S:\n",
    "        π[s] = argmax over actions a of:\n",
    "               R(s, a) + γ * sum over s' of P(s' | s, a) * Vₖ[s']\n",
    "\n",
    "    return Vₖ, π"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "07a941e2-33c9-49d3-84ac-3373b8f33f19",
   "metadata": {},
   "source": [
    "## 2. Implementation Used in This Project\n",
    "\n",
    "The implementation in this project follows the same Bellman update principle but is adapted for practical use and clarity in code."
   ]
  },
  {
   "cell_type": "raw",
   "id": "337e86ff-5bf0-452f-95ae-cb13123ef1c4",
   "metadata": {},
   "source": [
    "\n",
    "procedure ValueIteration(S, A, P, R, γ, θ)\n",
    "\n",
    "    initialize V[s] = 0 for all s in S\n",
    "\n",
    "    repeat:\n",
    "        Δ = 0\n",
    "\n",
    "        for each state s in S:\n",
    "\n",
    "            if s has no available actions:\n",
    "                continue\n",
    "\n",
    "            best_value = -∞\n",
    "\n",
    "            for each action a in A(s):\n",
    "\n",
    "                total = 0\n",
    "\n",
    "                for each (probability p, next state s') in P(s, a):\n",
    "                    total += p * (R(s, a, s') + γ * V[s'])\n",
    "\n",
    "                best_value = max(best_value, total)\n",
    "\n",
    "            Δ = max(Δ, |V[s] - best_value|)\n",
    "            V[s] = best_value\n",
    "\n",
    "    until Δ < θ\n",
    "\n",
    "    for each state s in S:\n",
    "\n",
    "        if s has no available actions:\n",
    "            π[s] = None\n",
    "            continue\n",
    "\n",
    "        best_action = None\n",
    "        best_value = -∞\n",
    "\n",
    "        for each action a in A(s):\n",
    "\n",
    "            total = 0\n",
    "\n",
    "            for each (p, s') in P(s, a):\n",
    "                total += p * (R(s, a, s') + γ * V[s'])\n",
    "\n",
    "            if total > best_value:\n",
    "                best_value = total\n",
    "                best_action = a\n",
    "\n",
    "        π[s] = best_action\n",
    "\n",
    "    return V, π"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "34df6ce2-6d6f-4c60-bff9-e1ebfdca359f",
   "metadata": {},
   "source": [
    "## 3. Differences\n",
    "\n",
    "While both versions are based on the same Bellman optimality equation, the implementation introduces some modifications.\n",
    "\n",
    "The first difference lies in how the value function is updated. The textbook uses a synchronous approach, maintaining two separate value functions ($V_k$) and ($V_{k-1}$). Each iteration is computed entirely from the previous one. In contrast, this implementation uses in-place updates, where a single value function ($V$) is updated directly. This allows newly computed values to be reused immediately, often improving convergence speed and simplifying the code.\n",
    "\n",
    "The second difference concerns the stopping condition. In Figure 9.16, the algorithm repeats until a general termination condition is met. Here, convergence is explicitly defined using a threshold ( $\\theta$ ), and the algorithm stops when the maximum change across all states falls below this value. This makes the behaviour of the algorithm precise and reproducible.\n",
    "\n",
    "Another key difference is the reward structure. The textbook assumes rewards of the form ($R(s,a)$), which depend only on the current state and action. In this implementation, rewards are defined as (R(s,a,s')), allowing them to depend on the resulting next state. This provides greater flexibility and is particularly useful in environments such as Grid World, where transitions can lead to different outcomes with different rewards.\n",
    "\n",
    "Additionally, terminal states are handled explicitly. States with no available actions are skipped during value updates and assigned a policy of None. This makes the implementation robust and avoids unnecessary computations.\n",
    "\n",
    "Finally, unlike some optimized implementations, policy extraction is performed after convergence."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
