import msgs
blkmsg = msgs.Blockmsg.fromjson({"type": "block", "txs": [{"inputs": [{"script": "04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73", "outpoint": {"index": 4294967295, "tx": "0000000000000000000000000000000000000000000000000000000000000000"}, "sequence": 4294967295}], "locktime": 0, "version": 1, "outputs": [{"amount": 5000000000, "script": "4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac"}]}], "block": {"nonce": 2083236893, "version": 1, "time": 1231006505, "merkle": "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b", "bits": 0x1d00ffff, "prev": "0000000000000000000000000000000000000000000000000000000000000000"}})

hash = blkmsg.block.hash

blkdata = "".join([
"010000000000000000000000000000000000000000000000000000000000000000000000",
"3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49",
"ffff001d1dac2b7c01010000000100000000000000000000000000000000000000000000",
"00000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f",
"4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f",
"6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104",
"678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f",
"4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000"])

blkmsg = msgs.Blockmsg.frombinary(blkdata.decode("hex"))[0]
hash = blkmsg.block.hash
