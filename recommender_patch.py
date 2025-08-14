# Auto-generated recommender patch demo

import math

def adjust_volatility(score: float) -> float:
    """Apply calibration to volatility preference score.
    This is a demo patch committed by the multi-agent workflow.
    """
    return min(1.0, max(0.0, score * 1.15 + 0.05))

if __name__ == '__main__':
    sample = 0.72
    print('Adjusted:', adjust_volatility(sample))
