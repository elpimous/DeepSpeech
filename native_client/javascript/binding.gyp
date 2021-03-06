{
  "targets": [
    {
      "target_name": "deepspeech",
      "sources": [ "deepspeech_wrap.cxx" ],
      "ldflags": [
        "-L$(TFDIR)/bazel-bin/tensorflow -L$(TFDIR)/bazel-bin/native_client"
      ],
      "libraries": [
        "-ldeepspeech", "-ldeepspeech_utils", "-ltensorflow_cc"
      ],
      "include_dirs": [
        "../"
      ]
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
}
  ]
}
