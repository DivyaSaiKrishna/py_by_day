from typing import List, Optional
from dataclasses import dataclass, field

R = 26  # Number of possible children (e.g., for an alphabetic trie)

@dataclass
class RTrieNode:
    value: int
    next_: List[Optional["RTrieNode"]] = field(default_factory=lambda: [None] * R)

    def __post_init__(self):
        if len(self.next_) != R:
            raise ValueError(f"Invalid length provided for next list")

# Example Usage
if __name__ == "__main__":
    root = RTrieNode(value=0)  # Root node
    root.next_[0] = RTrieNode(value=1)  # Adding a child node
    root.next_[1] = RTrieNode(value=2)  # Adding another child node

    print(f"Root Node Value: {root.value}")
    print(f"Child 1 Value (index 0): {root.next_[0].value}")
    print(f"Child 2 Value (index 1): {root.next_[1].value}")
