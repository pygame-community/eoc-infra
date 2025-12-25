NOTE: I use colons as a delimiter between GH users and one of ther repositories, e.g. `ddorn:eoc-dev`.

This proposal separates WeeklyChallenges ( <https://github.com/pygame-community/LegacyWeeklyChallenges> ) into 5 separate repositories and rebrands it as Era of Challenges ( <https://github.com/pygame-community/EraOfChallenges> ).

## Delegating the "development repository" responsibilty

`pygame-community:LegacyWeeklyChallenges` should no longer be the repository to fork to participate in era of challenges.

Instead, a new GitHub repository should be created called `pygame-community:eoc-dev` . This allows people to simply instantiate a repository for working on challenges by forking it, which would come preconfigured with everything needed to work on specific challenges. As time passes, participants will be able to join new challenges by fetching new branches for those challenges. EOC challenge branches would be of the form `eoc<xxx>_challenge_name/template`  (`xxx` will be a three digit number with leading zeros if necessary, and can be continually expanded to more digits as needed), e.g. `eoc007_matrixrain/template`. These templates would be provided by challenge creators.

To start working on a challenge inside a `<username>:eoc-dev` fork (e.g. `ddorn:eoc-dev`), a user would need to fetch the newest template branches from `eoc-dev`, e.g. `git fetch upstream`  (`upstream` is `pygame-community:eoc-dev`, while `origin` would be the fork of the form `<username>:eoc-dev`). They would then check-out their target template branch and make a new branch from it to work with, e.g.:

```sh
git remote add upstream "https://github.com/pygame-community/eoc-dev"
git fetch upstream
git switch eoc007_matrixrain/template
git switch -c eoc007_matrixrain/ddorn # will create a new branch and switch to it
```

The steps above can be implemented in a CLI too, in the form of `python -m eoc init 006` (prepare challenge 006 locally).

The overall structure for a template branch would be as follows:

```txt
 /
  ┣ eoc<xxx>_challenge_name/ # the source code folder (mandatory)
  ┃  ┣ __init__.py # The only permitted entry point
  ┃  ┣ ...
  ┣ challenge.json
  ┣ requirements.txt
  ┗ README.md             # contains challenge instructions
```

## Delegating the "submission repository" responsibilty

`pygame-community:LegacyWeeklyChallenges` should no longer be the repository to use for challenge submissions.

Instead, submission should occur by opening PRs to `pygame-community:eoc-submissions` from a fork of the form `<username>:eoc-dev`, tagged with their challenge number as a label and submitted in a timely manner. Submissions would introduce branches of the form `eoc<xxx>_challenge_name/<username>` (e.g. `eoc007_matrixrain/ddorn`)  into the `eoc-submissions` repository.

## Delegating the "Era of Challenges Library" responsibilty

`pygame-community:LegacyWeeklyChallenges` should no longer be the repository that contains `wclib`.  Instead, 2 new repositories should be created called [`pygame-community:eoc-infra`](https://github.com/pygame-community/eoc-infra) and [`pygame-community:eoc.challenges`](https://github.com/pygame-community/eoc.challenges). The former will be a monorepo containing a helper CLI tool for submission called `eoc` and a library for managing challenge-agnostic infrastructure called `eoclib`, while the latter will host challenge-specific helper tools and assets on a separate branch per challenge.

`eoc.challenges` will be a [namespace package](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/), whose contained modules make use of `eoclib` inside `pygame-community:eoc-infra`, and host the code and assets for every challenge as they are downloaded by participants from GitHub for their challenge entries (assets like images and audio will be included in the package using a `MANIFEST.in` file and similar mechanisms: <https://python-packaging.readthedocs.io/en/latest/non-code-files.html>, <https://setuptools.pypa.io/en/stable/userguide/datafiles.html#package-data>). Each of those branches would be of the form `eoc<xxx>_challenge_name` (same as the challenge name). Installing them would look like this: `pip install "eoc.challenges.eoc007_matrixrain @ git+https://github.com/pygame-community/eoc.challenges@eoc007_matrixrain.git"`. These strings will be exposed inside template branches of `pygame-community:eoc-dev` in `requirements.txt` files.

Era of Challenges challenge entries should import these editions as follows: `import eoc.challenges.eoc007_matrixrain as eoc007`. `eoc007.assets.audio` and `eoc007.assets.images` would both expose string constants that map to the assets, e.g. `eoc007.assets.images.PLAYER`.

## Delegating the "Era of Challenges Client" responsibilty

`pygame-community:EraOfChallenges` should only act as a "player" for playing Weekly Challenges. To avoid people having to download `pygame-community:eoc-submissions` or anything similar, the program would download challenge files on demand from GitHub (`https://github.com/pygame-community/pygame-ce/archive/refs/heads/eoc007_matrixrain/ddorn.zip`), and keep them around in a locally generated cache of the form `.eoccache/eoc<xxx>_challenge_name/<username>/*` .

To make this work, 3 requirements have to be met:

1. Each challenge-specific branch of `pygame-community:eoc.challenges` must have a `challengeinfo.json` file describing a challenge and what achievements it supports.

2. Each challenge submission branch of a participant (`eoc<xxx>_challenge_name/<username>`) will need a top level `challenge.json` file containing any important challenge metadata (e.g. submitter usernames). It will be generated by a script (e.g. `python3 -m eoc submit`) that triggers an interactive CLI prompt, asking questions relevant to the needed `challenge.json` fields (supported achievements would be looked up inside `eoc<xxx>_challenge_name/info`, e.g. `https://cdn.jsdelivr.net/gh/pygame-community/eoc.challenges@eoc007_matrixrain/challengeinfo.json`), as well as prompting for whether repetitive data should be stored inside of Git's repository-level config data if not already present (stored as `git config --local user.name <username>` / `git config --local user.discord_username <Discord username>`, read as `git config --local --get user.name <username>` / `git config --local --get user.discord_username <discord_username>`).

    An initial `challenge.json` could look like this:

    ```jsonc
    {
        "github_username": "...", // (required)
        "discord_username": "...", // (optional)
        "display_name": "...", // A preferred display name (optional)
        "achievements": [
           // achievement field names
        ],
    }
    ```

3. Each challenge must have a corresponding branch in `pygame-community/eoc-submissions` called `eoc<xxx>_challenge_name/info`, which itself contains a `submitters.txt` file (queried as `https://cdn.jsdelivr.net/gh/pygame-community/eoc-submissions@eoc007_matrixrain/info/submitters.txt`) listing up GitHub usernames of users who submitted, in order to build links like `https://github.com/pygame-community/eoc-submissions/archive/refs/heads/eoc007_matrixrain/ddorn.zip` to download a user's submission code and `challenge.json`, with `eoc<xxx>_challenge_name/__init__.py` serving as the entry point for `EraOfChallenges` to load a user's submission as a module at runtime. This `submitters.txt` file would be automatically updated by a GitHub Action inside `pygame-community:eoc-submissions` that triggers on every PR merge with branch names matching `eoc<xxx>_challenge_name/<username>`, appending the submitter's GitHub username to the file if not already present.

All in all, these changes would lead to a far more scalable future for Era of Challenges.

```mermaid
---
config:
  layout: fixed
  theme: neutral
---
flowchart TB
 subgraph user_repo["Type: Repo"]
        u_dev{{"user:eoc-dev"}}
        u_dev_desc@{ label: "Holds a participant's code for challenges, branched per challenge (e.g. `user:eoc-dev:eoc007_matrixrain/ddorn`). Receives templates & infra via pulls. Submissions are PR'd to the community." }
  end
 subgraph user_app["Type: Application"]
        u_app(["user:EraOfChallenges"])
        u_app_desc["Local client for playing challenges. Downloads templates and user submissions from the official repos."]
  end
 subgraph user["user"]
        user_repo
        user_app
  end
 subgraph infra_repo["Type: Repo"]
        c_infra{{"pygame-community:eoc-infra"}}
        c_infra_desc@{ label: "Infra monorepo. Hosts shared CLI (`eoc`) and `eoclib`, the challenge-agnostic infrastructure library." }
  end
 subgraph eoclib_repo["Type: Repo"]
        c_eoclib{{"pygame-community:eoc-infra:eoclib"}}
        c_eoclib_desc["Core infrastructure library used by templates, submissions, and challenge helpers."]
  end
 subgraph warelib_repo["Type: Repo"]
        c_warelib{{"pygame-community:warelib"}}
        c_warelib_desc@{ label: "Foundation infrastructure library for `pygame-community:eoc-infra:eoclib`." }
  end
 subgraph cli_repo["Type: Repo"]
        c_cli{{"pygame-community:eoc-infra:eoc"}}
        c_cli_desc["CLI tool for interactive submission automation and metadata generation."]
  end
 subgraph challenges_repo["Type: Repo"]
        c_challenges{{"pygame-community:eoc.challenges"}}
        c_challenges_desc@{ label: "Challenge-specific APIs and assets, one branch per challenge (e.g. `eoc007_matrixrain`)." }
  end
 subgraph dev_repo["Type: Repo"]
        c_dev{{"pygame-community:eoc-dev"}}
        c_dev_desc@{ label: "Template repository. Each challenge is a branch (e.g. `eoc007_matrixrain/template`)." }
  end
 subgraph submissions_repo["Type: Repo"]
        c_sub{{"pygame-community:eoc-submissions"}}
        c_sub_desc@{ label: "Central submission repo. PRs introduce branches (e.g. `eoc007_matrixrain/ddorn`)." }
  end
 subgraph player_repo["Type: Repo"]
        c_player{{"pygame-community:EraOfChallenges"}}
        c_player_desc["Desktop client for browsing, downloading, and playing challenge submissions."]
  end
 subgraph community["pygame-community"]
        infra_repo
        eoclib_repo
        warelib_repo
        cli_repo
        challenges_repo
        dev_repo
        submissions_repo
        player_repo
  end
    dev_repo -- Forked/cloned by users to start challenges --> user_repo
    eoclib_repo -- Provides shared infrastructure library to --> dev_repo & challenges_repo
    cli_repo -- Provides submission automation tooling to --> user_repo & dev_repo
    challenges_repo -- "Provides challenge-specific APIs & assets to (e.g. `import eoc.challenges.eoc007_matrixrain as eoc007`)" --> dev_repo
    challenges_repo -- "Provides challenge-specific APIs & assets to" --> user_repo
    user_repo -- "Submissions are opened as PRs into (e.g. `eoc007_matrixrain/ddorn`)" --> submissions_repo
    submissions_repo -- "Submissions are downloaded on demand by (e.g. `.../archive/refs/heads/eoc007_matrixrain/ddorn.zip`)" --> player_repo
    challenges_repo -- Challenge assets are downloaded on demand by --> player_repo
    player_repo -- "Downloaded code/assets are cached locally by (e.g. `.eoccache/eoc007_matrixrain/ddorn/*`)" --> user_app
    warelib_repo -- Core dependency of --> eoclib_repo
    infra_repo -- Is monorepo for --> eoclib_repo & cli_repo

    u_dev_desc@{ shape: rect}
    c_infra_desc@{ shape: rect}
    c_warelib_desc@{ shape: rect}
    c_challenges_desc@{ shape: rect}
    c_dev_desc@{ shape: rect}
    c_sub_desc@{ shape: rect}
    style u_dev_desc stroke-dasharray: 4
    style u_app_desc stroke-dasharray: 4
    style c_infra_desc stroke-dasharray: 4
    style c_eoclib_desc stroke-dasharray: 4
    style c_cli_desc stroke-dasharray: 4
    style c_challenges_desc stroke-dasharray: 4
    style c_dev_desc stroke-dasharray: 4
    style c_sub_desc stroke-dasharray: 4
    style c_player_desc stroke-dasharray: 4
```
