### Text Formatting for Monokai ST3
```javascript
"workbench.colorTheme": "Monokai ST3",

    "editor.tokenColorCustomizations": {
        "textMateRules": [
                {
                "scope": [
                    "keyword.control"
                ],
                "settings": {
                    "fontStyle": "italic"
                }
            }
        ]
    },

```

### Disable Gitlens CodeLens
```javascript
    "gitlens.currentLine.enabled": false,
    "gitlens.hovers.currentLine.over": "line",
    "gitlens.codeLens.enabled": false,
    "git.autofetch": true,
```


### Fix Python Linting
```javascript
    "python.linting.pylintArgs": [
        "--errors-only",
        "--generated-members=numpy.* ,torch.* ,cv2.* , cv.*"
        ],
```

### Vim EasyMotion Bindings
```javascript
    "vim.easymotion": true,
    "vim.normalModeKeyBindingsNonRecursive": [
        {
            "before": [" "],
            "after": ["<leader>", "<leader>", "<leader>", "b", "d", "w"]     
        }
    ]
```