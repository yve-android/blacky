[33mcommit 04975261a2b7e9f12c49c6c683a6f1b028d665ac[m[33m ([m[1;36mHEAD[m[33m -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: yve-android <yvonne26sa90@gmail.com>
Date:   Wed Dec 31 10:02:22 2025 +0100

    Fix: Pin actions to commit SHA

[33mcommit 7a98bc2688df9966cd75c3682f3342d90b44ac64[m
Author: yve-android <yvonne26sa90@gmail.com>
Date:   Tue Dec 30 11:05:01 2025 +0100

    tools: add GitHub Actions compliance fixer

[33mcommit 9d34cbf299295fb3e0467ab36c0deb9063851457[m
Author: yve-android <yvonne26sa90@gmail.com>
Date:   Tue Dec 30 10:35:49 2025 +0100

    Fix: Pin actions to commit SHA

[33mcommit fcf8feee6561f7fda6ee63943caa44acbf8235f1[m
Author: Yve-android <yvonne26sa90@gmail.com>
Date:   Mon Dec 29 01:11:59 2025 +0100

    Create codeql.yml

[33mcommit 680a047672d79ea8f923905196f2806bed8f14bb[m
Merge: 741e49e 9bd8483
Author: Yve-android <yvonne26sa90@gmail.com>
Date:   Sun Dec 28 23:44:52 2025 +0100

    Potential fix for code scanning alert no. 1: Workflow does not contain permissions (#30)
    
    Potential fix for
    [https://github.com/yve-android/blacky/security/code-scanning/1](https://github.com/yve-android/blacky/security/code-scanning/1)
    
    In general, fix this by adding an explicit `permissions:` block that
    grants only the minimal scopes needed. Since this workflow only needs to
    read repository contents (for `actions/checkout`) and upload an artifact
    (which does not require repository write access), `contents: read` is
    sufficient.
    
    The best single fix without changing functionality is to add a
    workflow-level `permissions:` block near the top of
    `.github/workflows/build-apk.yml`, so it applies to all jobs. Place it
    after the `name:` (line 1) and before `on:` (line 3), with:
    
    ```yaml
    permissions:
      contents: read
    ```
    
    No additional imports, methods, or definitions are needed because this
    is purely a YAML configuration change within the workflow file.
    
    
    _Suggested fixes powered by Copilot Autofix. Review carefully before
    merging._

[33mcommit 9bd84833464685f7b911eac0752f3bddb5d4cba5[m
Merge: d1f07bf 741e49e
Author: Yve-android <yvonne26sa90@gmail.com>
Date:   Sun Dec 28 23:44:43 2025 +0100

    Merge branch 'blacky' into alert-autofix-1
