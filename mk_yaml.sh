#TODO: branch of $RUNTYPE
python -c "print(open('template.yaml').read().format(DB='$PWD/databses/test',NO_STAR='true',PROJDIR='$PWD'))"
