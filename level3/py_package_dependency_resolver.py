def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []

    indegree = {}

    dependents = {}

    for package in packages:
        indegree[package] = 0
        dependents[package] = []

    for package, dependencies in packages.items():
        for dependency in dependencies:
            if dependency in packages:
                indegree[package] += 1
                dependents[dependency].append(package)

    ready = []

    for package in indegree:
        if indegree[package] == 0:
            ready.append(package)

    ready.sort()

    result = []

    while ready:
        package = ready.pop(0)
        result.append(package)

        for dependent in dependents[package]:
            indegree[dependent] -= 1

            if indegree[dependent] == 0:
                ready.append(dependent)

        ready.sort()

    if len(result) != len(packages):
        return []

    return result