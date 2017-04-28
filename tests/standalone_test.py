#!/usr/bin/env python
import os
import struct
import time
from panda.lib.panda import Panda

if __name__ == "__main__":
  if os.getenv("WIFI") is not None:
    p = Panda("WIFI")
  else:
    p = Panda()
  print p.health()

  a = 0
  while 1:
    # flood
    msg = "\xaa"*4 + struct.pack("I", a)
    p.can_send(0xaa, msg, 0)
    p.can_send(0xaa, msg, 1)
    p.can_send(0xaa, msg, 4)
    time.sleep(0.01)

    print p.can_recv()
    a += 1
