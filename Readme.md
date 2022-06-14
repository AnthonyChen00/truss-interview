# CSV Normalizer

## Description:

My solution for the coding problem: [CSV normalization](https://github.com/trussworks/truss-interview/blob/main/CSV_README.md)

## Build/Run:
### Dev
Used VS Code Remote Containers/devcontainers to build a dev environment

### Run
Please run `the normalizer.py` script like this:
```
python3 normalizer.py < {input csv} > {output csv}
```

### Coding Notes/Thought Process
1. Read over & understanding the normalizing requirements
2. Determine how pipe works with python 
3. Determine how to read csv file 
4. Handle converting timezone 
5. Zero pad zip code
6. Convert time stamps 
7. Test output 
8. Determine important value verifcation
9. Determine how to handle unicode decode errors
10. Determine why test set is working (changed the file encoding - defaulted utf8)
11. Added decode/replacement character


total time: 
2:50 hrs