from importlib.metadata import version, distributions
from packaging import version as Version
import sys
import subprocess

def is_package_compatible(package_name, version_str):
    try:
        import pkg_resources
        requirement = f"{package_name}=={version_str}"
        pkg_resources.require(requirement)
        return True
    except Exception:
        return False

def check_compatibility():
    try:
        with open('requirements.txt', 'r', encoding='utf-8-sig') as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        incompatible = []
        missing_packages = []
        
        for req in requirements:
            try:
                package_name = req.split('==')[0]
                required_version = req.split('==')[1] if '==' in req else None
                
                try:
                    installed_version = version(package_name)
                    if package_name == 'pymysql':
                        # PyMySQL versions known to work with Python 3.10
                        compatible_versions = ['1.0.2', '1.0.3']
                        if installed_version not in compatible_versions:
                            incompatible.append(f"{package_name}: installed version {installed_version} may not be compatible with Python 3.10. Recommended versions: {', '.join(compatible_versions)}")
                    elif required_version and Version.parse(installed_version) != Version.parse(required_version):
                        incompatible.append(f"{package_name}: required={required_version}, installed={installed_version}")
                    print(f"Checking {package_name}: required={required_version}, installed={installed_version}")
                except Exception:
                    missing_packages.append(package_name)
                    print(f"Package {package_name} is not installed")
            except Exception as e:
                incompatible.append(f"{req}: {str(e)}")
        
        if missing_packages:
            print("\nMissing packages:")
            for pkg in missing_packages:
                print(f"- {pkg}")
            print("\nTo install missing packages, run:")
            print("pip install -r requirements.txt")
        
        if incompatible:
            print("\nIncompatible packages found:")
            for pkg in incompatible:
                print(f"- {pkg}")
        else:
            print("\nAll packages are compatible!")
    except FileNotFoundError:
        print("Error: 'requirements.txt' file not found.")
        return

def check_python_version():
    required_version = (3, 10)
    current_version = sys.version_info[:2]
    if current_version < required_version:
        print(f"Python {required_version[0]}.{required_version[1]} or higher is required")
        print(f"Current version: {current_version[0]}.{current_version[1]}")
        return False
    return True

if __name__ == "__main__":
    if check_python_version():
        print(f"Python {sys.version_info.major}.{sys.version_info.minor} detected")
        check_compatibility()
