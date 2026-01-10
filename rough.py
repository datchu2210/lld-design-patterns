# INTERVIEW QUESTION: THREAD-SAFE LAZY SINGLETON
# Problem Statement

# You are designing a configuration manager for a backend service.

# Requirements

# Only one instance of the configuration manager should exist.

# The instance must be created lazily (only when first requested).

# The implementation must be thread-safe.

# Direct object creation using the constructor should be prevented.

# Multiple threads calling getInstance() at the same time must never create more than one instance.

import threading

class ConfigurationManager:
    __instance  = None

    __lock = threading.Lock()

    def __init__(self):
        if ConfigurationManager.__instance is not None:
            raise Exception("Already Configured")
        

    def getInstance():
        if ConfigurationManager.__instance is None:
            with ConfigurationManager.__lock:
                if ConfigurationManager.__instance is None:
                    ConfigurationManager.__instance = ConfigurationManager.__new__(ConfigurationManager)
        return ConfigurationManager.__instance
    
obj1 = ConfigurationManager()
obj1.getInstance()
obj2 = ConfigurationManager()
obj2.getInstance()