def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    if not packages:
        return []

    # Number of dependencies for each package
    indegree = {}

    # Packages that depend on each package
    dependents = {}

    for package in packages:
        indegree[package] = 0
        dependents[package] = []

    # Build the graph
    for package, dependencies in packages.items():
        for dependency in dependencies:
            if dependency in packages:
                indegree[package] += 1
                dependents[dependency].append(package)

    # Packages with no dependencies
    ready = []

    for package in indegree:
        if indegree[package] == 0:
            ready.append(package)

    ready.sort()

    result = []

    while ready:
        # Alphabetically first package
        package = ready.pop(0)
        result.append(package)

        # Remove this package as a dependency
        for dependent in dependents[package]:
            indegree[dependent] -= 1

            if indegree[dependent] == 0:
                ready.append(dependent)

        ready.sort()

    # If not all packages were processed, there is a cycle
    if len(result) != len(packages):
        return []

    return result