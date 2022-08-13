rm -rf docs
mkdir docs
doxygen clrs/py/doxygen.config
doxygen clrs/cpp/doxygen.config
doxygen clrs/csharp/doxygen.config
