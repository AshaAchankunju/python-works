# 3.Pattern print 
#         * 
#       *   * 
#     *   *   * 
#   *   *   *   * 
# *   *   *   *   *

# for row in range(1,6):
#     for spc in range(6-row):
#         print(" ",end="")
#     for col in range(1,row+1):
#         print("* ", end="")
        
#     print()

# 3.Pattern print 
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *



for row in range(1, 6):
    for spc in range(6 - row):
        print("  ", end="")
    for col in range(1, row + 1):
        print("* ", end="")

    print()