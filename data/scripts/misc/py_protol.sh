# Reference: https://github.com/ApolloAuto/apollo/issues/14666#issuecomment-1303042647

function build_py_proto() {
  if [ -d "./py_proto" ];then
    rm -rf py_proto
  fi
  mkdir py_proto

  find modules/common_msgs/ -name "*.proto" \
    | grep -v node_modules \
    | xargs protoc --python_out=py_proto

  find modules/common_msgs/ -name "*.proto" \
    | grep -v node_modules \
    | xargs protol --create-package --in-place --python-out=py_proto protoc --proto-path=/home/yuqi/ResearchWorkspace/AV_Research/eDoppelTest/data/apollo/
}

build_py_proto
