#=========================================================================
# parcv2 beq tests
#=========================================================================

from pymtl import *

from pclib.SparseMemoryImage import SparseMemoryImage

#---------------------------------------------------------------------------
# String based Assembly Tests
#---------------------------------------------------------------------------
# Directed string based assembly tests

# test_start string

test_start = """
  .text;
  .align  4;
  .global _test;
  .ent    _test;
  _test:
"""

# test_end string

test_end   = """
  .end    _test;
"""

def beq_asm():

  asm_str = \
    ( test_start +
       """
       li    $2, 1
       li    $3, 1
       beq   $2, $3, 1f
       jal   2f
       mtc0  $4, $1
       nop
       nop
       nop
       nop
    1: mtc0  $3, $1
    2: nop; nop; nop; nop;
       nop; nop; nop; nop;
       """
     + test_end )

  mem_delay       = 0
  sparse_mem_img  = SparseMemoryImage( asm_str = asm_str )
  expected_result = 1

  return [ mem_delay, sparse_mem_img, expected_result ]

#---------------------------------------------------------------------------
# VMH File Assembly Tests
#---------------------------------------------------------------------------
# Self-checking VMH file based assembly tests

# VMH Files location

vmh_dir = '../tests/build/vmh/'

# test with no delay

def beq_vmh_delay0():

  test_file = vmh_dir + 'parcv2-beq.vmh'

  mem_delay       = 0
  sparse_mem_img  = SparseMemoryImage( vmh_filename = test_file )
  expected_result = 1

  return [ mem_delay, sparse_mem_img, expected_result ]

# test with delay

def beq_vmh_delay5():

  test_file = vmh_dir + 'parcv2-beq.vmh'

  mem_delay       = 5
  sparse_mem_img  = SparseMemoryImage( vmh_filename = test_file )
  expected_result = 1

  return [ mem_delay, sparse_mem_img, expected_result ]
