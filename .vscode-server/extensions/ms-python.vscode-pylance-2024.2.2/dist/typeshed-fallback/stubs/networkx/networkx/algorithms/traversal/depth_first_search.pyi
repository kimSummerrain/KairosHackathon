from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node

def dfs_edges(
    G: Graph[_Node], source: _Node | None = None, depth_limit: int | None = None
) -> Generator[tuple[_Node, _Node], None, None]: ...
def dfs_tree(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None): ...
def dfs_predecessors(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None): ...
def dfs_successors(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None): ...
def dfs_postorder_nodes(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None): ...
def dfs_preorder_nodes(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None): ...
def dfs_labeled_edges(G, source: Incomplete | None = None, depth_limit: Incomplete | None = None) -> None: ...
