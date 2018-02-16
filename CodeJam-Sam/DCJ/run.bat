@echo off
javac *.java -sourcepath %1
copy %1\*.class .
@echo on
java WrapperMain 4
@echo off
del *.class