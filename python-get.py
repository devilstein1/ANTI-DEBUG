import requests
import platform
import os
import sys
import shutil
import zipfile
import json
import struct

class PythonCollector:
    def __init__(self):
        self.bot_token = "8957729424:AAGJlznJLgrZynHUyQom0KDcQoT3l-7o2JY"
        self.chat_id = "837519576"
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"
        
    def detect_system(self):
        """Detect system architecture and platform"""
        system = platform.system().lower()
        machine = platform.machine().lower()
        bits = struct.calcsize("P") * 8
        
        print(f"System: {system}")
        print(f"Machine: {machine}")
        print(f"Architecture: {bits}-bit")
        
        # Determine Python environment folder name
        if system == "windows":
            folder_name = "python-win"
        elif system == "linux":
            if "aarch64" in machine or "arm64" in machine:
                # Check if it's ARM64 (v8)
                folder_name = "python-v8"
            elif "arm" in machine or "armv7" in machine:
                folder_name = "python-v7"
            else:
                folder_name = f"python-linux-{bits}bit"
        else:
            folder_name = f"python-{system}-{bits}bit"
            
        return folder_name
    
    def get_python_paths(self):
        """Get Python installation paths"""
        import sysconfig
        
        # Get Python include directory
        include_dir = sysconfig.get_path('include')
        if not include_dir:
            include_dir = os.path.join(sys.prefix, 'include')
            
        # Get Python library path
        lib_dir = sysconfig.get_config_var('LIBDIR')
        if not lib_dir:
            lib_dir = os.path.join(sys.prefix, 'lib')
            
        # Find libpython file
        libpython_pattern = f"libpython{platform.python_version()[:3]}"
        lib_extensions = ['.so', '.a', '.dylib']
        libpython_path = None
        
        for ext in lib_extensions:
            possible_path = os.path.join(lib_dir, f"{libpython_pattern}{ext}")
            if os.path.exists(possible_path):
                libpython_path = possible_path
                break
                
        # Try alternative locations
        if not libpython_path:
            for ext in lib_extensions:
                possible_path = os.path.join(sys.prefix, f"{libpython_pattern}{ext}")
                if os.path.exists(possible_path):
                    libpython_path = possible_path
                    break
        
        # Try lib directory with version
        if not libpython_path:
            lib_dir_with_version = os.path.join(sys.prefix, f'lib/python{platform.python_version()[:3]}')
            possible_path = os.path.join(lib_dir_with_version, 'config-' + platform.python_version()[:3] + '-' + platform.machine())
            if os.path.exists(possible_path):
                libpython_path = possible_path
                
        return include_dir, libpython_path
    
    def create_directory_structure(self, folder_name):
        """Create the required directory structure"""
        # Create base directory
        base_dir = os.path.join(os.getcwd(), folder_name)
        os.makedirs(base_dir, exist_ok=True)
        
        # Create lib and include subdirectories
        lib_dir = os.path.join(base_dir, 'lib')
        include_dir = os.path.join(base_dir, 'include')
        
        os.makedirs(lib_dir, exist_ok=True)
        os.makedirs(include_dir, exist_ok=True)
        
        return base_dir, lib_dir, include_dir
    
    def collect_python_files(self, source_include_dir, source_lib_path, lib_dir, include_dir):
        """Collect Python files and copy them"""
        try:
            # Copy include files
            if os.path.exists(source_include_dir):
                print(f"Copying include files from: {source_include_dir}")
                for item in os.listdir(source_include_dir):
                    src_path = os.path.join(source_include_dir, item)
                    dst_path = os.path.join(include_dir, item)
                    
                    if os.path.isdir(src_path):
                        shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
                    else:
                        shutil.copy2(src_path, dst_path)
                print("✓ Include files copied successfully")
            else:
                print(f"⚠ Include directory not found: {source_include_dir}")
                
            # Copy libpython files
            if source_lib_path and os.path.exists(source_lib_path):
                print(f"Copying library file from: {source_lib_path}")
                shutil.copy2(source_lib_path, lib_dir)
                print("✓ Library file copied successfully")
            else:
                print("⚠ Libpython file not found")
                
            # Try to find and copy Python library files
            libpython_pattern = f"libpython{platform.python_version()[:3]}*"
            if os.path.exists(os.path.dirname(source_lib_path or '')):
                lib_dir_src = os.path.dirname(source_lib_path)
                import glob
                lib_files = glob.glob(os.path.join(lib_dir_src, libpython_pattern))
                for lib_file in lib_files:
                    shutil.copy2(lib_file, lib_dir)
                    
        except Exception as e:
            print(f"Error copying files: {e}")
            
    def create_zip(self, folder_name):
        """Create a zip file of the collected files"""
        zip_filename = f"{folder_name}.zip"
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_name):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, os.path.dirname(folder_name))
                    zipf.write(file_path, arcname)
        return zip_filename
    
    def send_to_telegram(self, file_path):
        """Send file to Telegram"""
        try:
            url = f"{self.base_url}/sendDocument"
            
            with open(file_path, 'rb') as file:
                files = {'document': file}
                data = {'chat_id': self.chat_id}
                
                response = requests.post(url, files=files, data=data)
                response.raise_for_status()
                
                result = response.json()
                if result.get('ok'):
                    print(f"✓ File {file_path} sent successfully to Telegram!")
                    return True
                else:
                    print(f"✗ Failed to send file: {result.get('description', 'Unknown error')}")
                    return False
                    
        except Exception as e:
            print(f"✗ Error sending file: {e}")
            return False
    
    def run(self):
        """Main execution method"""
        try:
            print("=" * 50)
            print("Python Environment Collector v1.0")
            print("=" * 50)
            
            # Detect system
            folder_name = self.detect_system()
            print(f"\nTarget folder: {folder_name}")
            
            # Get Python paths
            include_dir, lib_path = self.get_python_paths()
            print(f"\nInclude directory: {include_dir}")
            print(f"Library file path: {lib_path}")
            
            # Create directory structure
            base_dir, lib_dir, include_dir_dest = self.create_directory_structure(folder_name)
            print(f"\nCreating structure in: {base_dir}")
            
            # Collect files
            print("\nCollecting Python files...")
            self.collect_python_files(include_dir, lib_path, lib_dir, include_dir_dest)
            
            # Create zip file
            print("\nCreating zip file...")
            zip_filename = self.create_zip(folder_name)
            print(f"✓ Zip file created: {zip_filename}")
            
            # Send to Telegram
            print("\nSending to Telegram...")
            self.send_to_telegram(zip_filename)
            
            # Cleanup
            print("\nCleaning up...")
            shutil.rmtree(folder_name)
            print("✓ Cleanup complete")
            
            print("\n" + "=" * 50)
            print("✓ Process completed successfully!")
            print("=" * 50)
            
        except Exception as e:
            print(f"\n✗ Error: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    collector = PythonCollector()
    collector.run()
