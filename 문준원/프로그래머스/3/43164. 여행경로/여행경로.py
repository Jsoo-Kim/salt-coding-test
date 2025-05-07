def solution(tickets):
    graph = {}
    for start, end in tickets:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)
    
    for key in graph:
        graph[key].sort(reverse=True)

    route = []
    stack = ['ICN']

    while stack:
        curr = stack[-1]
        if curr in graph and graph[curr]:
            stack.append(graph[curr].pop())
        else:
            route.append(stack.pop())

    return route[::-1]