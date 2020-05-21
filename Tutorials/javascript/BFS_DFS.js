/*
Sections:
1. BFS
2. DFS
3. Example with this graph (numbers are represenative of nodes)
*/

// 1. BFS START ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// Runtime: O(E + V) which is basically O(max(E,V))
function doBFS(graph, rootIdx) {
  // initializing return statement (Runtime: O(V) where V is the number of vertexes of the graph)
  const bfsInfo = [];
  for (let i = 0; i < graph.length; i++) {
    bfsInfo[i] = {
      distance: null,
      parent: null
    };
  }

  // perform breadth-first search
  bfsInfo[rootIdx].distance = 0;
  const queue = [rootIdx];

  // Runtime at most O(V) because each vertex can be queued at most once
  while (queue.length > 0) {
    const curr = queue.shift();
    const neighborNodes = graph[curr];
    // Runtime O(E) where is the number of edges in the graph
    for (let i = 0; i < neighborNodes.length; i++) {
      const next = neighborNodes[i];
      if (bfsInfo[next].distance === null) {
        bfsInfo[next].parent = curr;
        bfsInfo[next].distance = bfsInfo[curr].distance + 1;
        queue.push(next);
      }
    }
  }
  // Total Runtime: O(V) + O(V) + O(E) = O(2V + E)
  // if 2V <= E: O(2V + E) <= O(2E) :. effective runtime O(E)
  // if 2V >= E: O(2V + E) <= O(4V) :. effective runtime O(V)
  return bfsInfo;
}

function printSearchInfo(searchInfo) {
  console.log('>>> BFS RESULTS:');
  for (let i = 0; i < searchInfo.length; i++) {
    const nEdges = searchInfo[i].distance;
    const prevVertex = searchInfo[i].parent;
    console.log(`Vertex ${i} was reached through vertex ${prevVertex} and is ${nEdges} edges away from the root vertex.`);
  }
  console.log('\n');
}


// 2. DFS START ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// NOTE: In this implementation,  I stuck with distance to keep track of visited vertices and
//  track the distance from the starting vertex. That said, this is not generally necessary
//  and a boolean tag 'visited' should surfice.
function dfs(graph, curr, dfsInfo, target) {
  // base case 1
  if (target && target < graph.length && dfsInfo[target].distance !== null) return;

  // search path in children vertices of current vertex.
  // Runtime: O(E)
  const neighborNodes = graph[curr];
  for (let i = 0; i < neighborNodes.length; i++) {
    const next = neighborNodes[i];

    // base case 2: Child already visited
    if (dfsInfo[next].distance !== null) continue;

    // continue recursion to grandchildren
    dfsInfo[next].parent = curr;
    dfsInfo[next].distance = dfsInfo[curr].distance + 1;
    dfs(graph, next, dfsInfo);
  }
}

function doDFS(graph, rootIdx, targetIdx) {

  const dfsInfo = [];
  for (let i = 0; i < graph.length; i++) {
    dfsInfo[i] = {
      distance: null,
      parent: null
    };
  }

  dfsInfo[rootIdx].distance = 0;

  dfs(graph, rootIdx, dfsInfo);

  if (targetIdx) {
    const pathExists = dfsInfo[targetIdx].distance !== null;
    console.log(`DFS RESULT: Path from vertex ${rootIdx} to vertex ${targetIdx} ${pathExists ? 'exists' : 'doesn\'t exists'}.`);
  }

  return dfsInfo;
}


/*

3. Example graphs:

  a) Bidirected graph with extraverted edges
    i.e. the edge 1--2 is points from 1->2 and 1<-2. 
      For the runtime calculation this would count as two edges.

      0--1--2
         | /
         |/
      3  4--5
*/
console.log('\nGraph A results:\n');

const exampleGraphA = [
  [1],
  [0, 2, 4],
  [1, 4],
  [],
  [1, 2, 5],
  [4]
];

// Run
printSearchInfo(doBFS(exampleGraphA, 1));
doDFS(exampleGraphA, 2, 3);
doDFS(exampleGraphA, 0, 5);

console.log('\nGraph B results:\n');

/*
  b) Graph with directed edges
    i.e. the edge 1->2 is a one-way street.

      0<-1<>2
      ^  ^
      |  |
      3->4->5
*/

const exampleGraphB = [
  [],
  [0, 2],
  [1],
  [0, 4],
  [1, 5],
  []
];


// Run
printSearchInfo(doBFS(exampleGraphB, 2));
doDFS(exampleGraphB, 2, 0);
doDFS(exampleGraphB, 0, 5);