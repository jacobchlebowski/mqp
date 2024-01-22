import vss

def create_shadow_copy(local_drives):
    return vss.ShadowCopy(local_drives)

def delete_shadow_copy(sc, specific_directory):
    # Delete shadow copies only for the specified directory
    sc.delete_specific(specific_directory)

# Create a set that contains the LOCAL disks you want to shadow
local_drives = set()
local_drives.add('C')

# Initialize the Shadow Copies
sc = create_shadow_copy(local_drives)

# An open and locked file we want to read
locked_file = r'C:\foo\bar.txt'
shadow_path = sc.shadow_path(locked_file)

# shadow_path will look similar to:
# u'\\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy7\\foo\\bar.txt'

# Open shadow_path just like a regular file
with open(shadow_path, 'rb') as fp:
    data = fp.read()

# When done with file operations, clean up the shadow copies for a specific directory
specific_directory = r'C:\foo'
delete_shadow_copy(sc, specific_directory)
