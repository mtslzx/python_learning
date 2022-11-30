def cat(inputFiles: str, outputFile: str) -> None:
    """
    concat files. inputFiles can be either str or list of str. outputFile must be str of file name.
    """
    outputFile = open(outputFile, 'w')
    for inputFile in inputFiles:
        with open(inputFile, 'r') as f:
            lines = f.readlines()
            for line in lines:
                outputFile.write(line)
    outputFile.close()
    return None


if __name__ == '__main__':
    cat(['./a.txt', './b.txt', './c.txt'], 'result.txt')

