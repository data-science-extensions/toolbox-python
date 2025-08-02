# Contribution Guidelines

All contributions are welcome! Please follow these guidelines to ensure a smooth contribution process.

## Overview

Here are some guidelines to help you get started:

1. **Raise an Issue**: Before starting work on a new feature or bug fix, please [raise an issue][new-issue] to discuss it. All enhancements and changes are discussed in the [issues section][issues]. This helps us avoid duplicate work and ensures that your contribution aligns with the project's goals.
2. **Check the issues and milestones**: Look at the [issues] and [milestones] to see if your contribution fits into the current roadmap.
3. **Fork the Repository**: [Create a fork][new-fork] of the repository to work on your changes. This allows you to make changes without affecting the main codebase.
4. **Create a new branch**: When working on a new feature or bug fix, [create a new branch][create-branch] from the `main` branch. Use a descriptive name for your branch that reflects the changes you are making.
5. **Clone the repository**: [Clone your forked repository][about-clone] to your local machine to start working on it.
6. **Creating your environment**: Set up your development environment according to the project's requirements. This may include installing dependencies, setting up virtual environments, and configuring tools like [uv][uv-installation], [pre-commit][pre-commit], [pytest][pytest], and [mypy][mypy].
7. **Make your changes**: Implement your changes in the new branch. Ensure that your code adheres to the project's coding standards and style guidelines.
8. **Commit your changes**: Commit your changes with a clear and descriptive commit message.
9. **Write tests**: If you are adding new features or fixing bugs, please write tests to ensure that your changes work as expected.
10. **Submit a Pull Request**: Once you have made your changes and committed them, [submit a pull][new-pr] request to the main repository. Provide a clear description of the changes you made and reference any related issues.


## Raise an Issue

If you find a bug or have a feature request, please [raise an issue][new-issue]. This helps us track and prioritize contributions effectively.

[<kbd>Raise an Issue</kbd>][new-issue]

When raising an issue, please follow these guidelines to ensure clarity and effectiveness:

1. **Title**: Provide a clear and concise title that summarizes the issue or feature request.
2. **Description**: Include a detailed description of the issue or feature request. Explain what the problem is, how it can be reproduced, and any relevant context.
3. **Steps to Reproduce**: If applicable, provide a step-by-step guide on how to reproduce the issue. This helps us understand the problem better.
4. **Expected vs Actual Behavior**: Describe what you expected to happen and what actually happened. This helps clarify the issue.
5. **Screenshots or Logs**: If possible, include screenshots or logs that illustrate the issue. This can be very helpful for debugging.
6. **Context**: Provide any additional context that might be relevant, such as the environment in which the issue occurred (e.g., operating system, Python version, etc.).


## Issues and Milestones

We are using [issues] to track bugs, feature requests, and enhancements, and [milestones] to organize these issues into manageable chunks.

If you want to contribute to the project, please check the current [issues] and [milestones] before starting work to ensure that your contribution aligns with the project's goals and priorities. This will help avoid duplication of effort and ensure that your contributions align with the project's roadmap. If you want to add something that is not already listed in the [milestones], please [raise an issue][new-issue] to discuss it first.

You can view the current [issues] and [milestones] on the project's GitHub page.

[<kbd>View Issues</kbd>][issues]

[<kbd>View Milestones</kbd>][milestones]


## Create a Fork

To contribute to this project, you need to [create a fork][new-fork] of the repository. This allows you to make changes without affecting the main codebase.

[<kbd>Create a Fork</kbd>][new-fork]


## Create a New Branch

When working on a new feature or bug fix, [create a new branch][create-branch] from the `main` branch. Use a descriptive name for your branch that reflects the changes you are making.

[<kbd>Create a New Branch</kbd>][create-branch]


## Clone the Repository

To start working on your forked repository, you need to [clone it][about-clone] to your local machine. This allows you to make changes and test them locally before submitting a pull request.


## Creating your Environment

When you are ready to start working on your changes, set up your development environment according to the project's requirements. In this project, we use [uv][uv] to manage the Python environments, [pre-commit][pre-commit] for code quality checks, and [pytest][pytest] for testing.

Follow these steps to set up your environment:

1. **Install uv**: Follow the instructions in the [uv installation guide][uv-installation] to install uv.
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
2. **Sync the environment**: Use [`uv`][uv] to set up the environment with the required dependencies.
    ```sh
    uv sync --all-groups --link-mode=copy
    ```
3. **Install pre-commit**: Install [pre-commit][pre-commit] to manage code quality checks.
    ```sh
    uv run --link-mode=copy pre-commit install
    ```
4. **Update pre-commit hooks**: Ensure that the pre-commit hooks are up to date.
    ```sh
    uv run --link-mode=copy pre-commit autoupdate
    ```


## Make Your Changes

Make your changes in the new branch you created. Ensure that your code adheres to the project's coding standards and style guidelines. If you are adding new features or fixing bugs, please write tests to ensure that your changes work as expected.

Ensure you follow the project's coding standards and style guidelines. This includes:

1. **Code Style**: Follow the [PEP 8][pep8] style guide for Python code.
2. **Docstrings**: Use clear and concise docstrings for all functions, classes, and modules. Ensure that they follow the [Google styleguide][google-docstrings].
3. **Testing**: Write unit tests for your code using [unittest][unittest] or [pytest][pytest]. Ensure that your tests cover all new functionality and edge cases.
4. **Code Coverage**: Maintain high code coverage for your tests. Use [Codecov][codecov] to check your coverage reports.
5. **Type Checking**: Use [mypy][mypy] for static type checking. Ensure that your code passes all type checks.

Because you have set up [`pre-commit`][pre-commit], these checks will be run automatically when you commit your changes. If any checks fail, you will need to fix them before you can successfully commit your changes. Further checks will also be run when you submit a pull request, so it's a good idea to ensure your code passes all checks before proceeding.


## Commit Your Changes

Once you have made your changes, commit them with a clear and descriptive commit message. This helps reviewers understand the purpose of your changes. A good commit message should:

- Start with a short summary of the changes (50 characters or less).
- Follow the summary with a blank line.
- Provide a detailed description of the changes, including why they were made and any relevant context.
- Use the imperative mood (e.g., "Add feature" instead of "Added feature").
- Reference any related issues or pull requests.
- Use bullet points or paragraphs to organize the description for readability.
- Avoid using vague terms like "fixes" or "changes" without context.
- Be concise but informative, providing enough detail for someone unfamiliar with the code to understand the changes.
- Avoid including unnecessary information or personal opinions.
- Use proper grammar and punctuation to enhance clarity.
- If applicable, include any relevant links to documentation or resources that provide additional context for the changes.
- If the commit is related to a specific issue, include the issue number in the commit message (e.g., "Fixes #123").
- If the commit is part of a larger feature or task, consider using a prefix like "feat:", "fix:", or "chore:" to categorize the commit (e.g., "feat: add new feature for user authentication").
- If the commit is a work in progress, consider using a prefix like "WIP:" to indicate that it is not yet complete (e.g., "WIP: start implementing new feature for user authentication").
- If the commit is a refactor or cleanup, consider using a prefix like "refactor:" to indicate that it does not introduce new functionality (e.g., "refactor: improve code readability and maintainability").
- If the commit is a documentation update, consider using a prefix like "docs:" to indicate that it only affects documentation (e.g., "docs: update README with installation instructions").
- If the commit is a test update, consider using a prefix like "test:" to indicate that it only affects tests (e.g., "test: add unit tests for new feature").

Ensure that any pre-commit checks pass before committing your changes. This includes code style checks, linting, and tests. If any checks fail, you will need to fix them before you can successfully commit your changes.


## Submit a Pull Request

Once you have made your changes and committed them, [submit a pull request][new-pr] to the main repository. Provide a clear description of the changes you made and reference any related issues.

When submitting a pull request, please follow these guidelines:

1. **Title**: Use a clear and descriptive title that summarizes the changes you made.
2. **Description**: Provide a detailed description of the changes you made, including:
   - What the changes do.
   - Why the changes were made.
   - Any relevant context or background information.
   - How to test the changes.
3. **Reference Issues**: If your changes address a specific issue, reference it in the pull request description (e.g., "Fixes #123" or "Closes #123).
4. **Link to Related Pull Requests**: If your changes are related to other pull requests, link to them in the description.
5. **Reviewers**: Optionally, you can request specific reviewers to review your pull request.
6. **Milestone**: Optionally, you can assign your pull request to a specific milestone if it is related to a larger feature or task.
7. **Check for Merge Conflicts**: Ensure that your branch is up to date with the main branch and that there are no merge conflicts. If there are conflicts, resolve them before submitting the pull request.
8.  **Be Responsive**: Be prepared to respond to feedback from reviewers. They may request changes or ask for clarification on certain aspects of your pull request. Address their comments promptly and respectfully.
9.  **Be Patient**: Reviewers may take some time to review your pull request, especially if they are busy with other tasks. Be patient and give them time to provide feedback.
10. **Follow Up**: After your pull request is merged, consider following up with any additional changes or improvements based on feedback from the review process. This helps maintain a high-quality codebase and shows that you are committed to improving the project.

[<kbd>Submit a Pull Request</kbd>][new-pr]


[issues]: https://github.com/data-science-extensions/toolbox-python/issues
[milestones]: https://github.com/data-science-extensions/toolbox-python/milestones
[new-issue]: https://github.com/data-science-extensions/toolbox-python/issues/new
[new-fork]: https://github.com/data-science-extensions/toolbox-python/fork
[create-branch]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository
[about-clone]: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
[about-pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[new-pr]: https://github.com/data-science-extensions/toolbox-python/compare
[uv]: https://docs.astral.sh/uv/
[uv-installation]: https://docs.astral.sh/uv/getting-started/installation/
[pre-commit]: https://pre-commit.com/
[pep8]: https://peps.python.org/pep-0008/
[google-docstrings]: https://google.github.io/styleguide/pyguide.html
[unittest]: https://docs.python.org/3/library/unittest.html
[pytest]: https://docs.pytest.org/
[codecov]: https://codecov.io/
[mypy]: https://mypy-lang.org/
