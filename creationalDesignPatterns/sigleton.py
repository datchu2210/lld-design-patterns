# ============================================================
# JudgeAnalytics Example – Class vs Instance Variables
# ============================================================

class JudgeAnalytics:
    # Class variable (shared across all objects of this class)
    submitCount = 0

    def __init__(self):
        # Instance variable (separate for each object)
        self.runCount = 0

    def incrementRunCount(self):
        self.runCount += 1

    def incrementSubmitCount(self):
        JudgeAnalytics.submitCount += 1

    def getRunCount(self):
        return self.runCount

    def getSubmitCount(self):
        return JudgeAnalytics.submitCount


analytics = JudgeAnalytics()
analytics.incrementRunCount()

analytics2 = JudgeAnalytics()
analytics2.incrementRunCount()

# From the above example, we can observe that:
# - runCount is an INSTANCE variable
# - Each object of JudgeAnalytics has its own runCount
# - runCount is NOT shared between different objects

# When shared state is required across the entire application,
# creating multiple instances becomes a problem.
# This is where the Singleton Pattern is useful.

# ============================================================
# Singleton Pattern
# ============================================================

# Singleton Pattern ensures that:
# - Only ONE instance of a class is created
# - That single instance is shared across the application

# ============================================================
# EAGER LOADING SINGLETON
# ============================================================

class EagerSingleton:
    # Class-level variable to store the single instance
    # Using __ makes it name-mangled to _EagerSingleton__instance,
    # which helps prevent accidental access from outside the class.
    __instance = None

    def __init__(self):
        # Prevents creation of more than one instance
        if EagerSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        # Store the instance when created for the first time
        EagerSingleton.__instance = self

    @staticmethod
    def getInstance():
        # Always returns the same instance
        return EagerSingleton.__instance


# Eager initialization:
# The instance is created at class load time.
# This happens even if the instance is never used.

# EagerSingleton._EagerSingleton__instance = EagerSingleton()
# print(EagerSingleton.getInstance())


# ============================================================
# LAZY LOADING SINGLETON
# ============================================================

# Lazy loading = Do NOT create the object until it is actually needed

class LazySingleton:
    _instance = None

    def __init__(self):
        # Prevent direct object creation using constructor
        raise Exception("Use getInstance() to access the singleton")

    @staticmethod
    def getInstance():
        # Instance is created ONLY on the first call to getInstance()
        if LazySingleton._instance is None:
            LazySingleton._instance = LazySingleton.__new__(LazySingleton)
            # In EAGER loading, instance creation happens when the class loads.
            # In LAZY loading, this line executes ONLY when getInstance()
            # is called for the first time.
        return LazySingleton._instance


# ============================================================
# EAGER vs LAZY – Key Differences
# ============================================================

# 🔴 Eager Singleton
# - Instance is created as soon as the class is loaded into memory
# - Object exists even if it is never used
# - Faster access, but may waste memory

# 🟢 Lazy Singleton
# - Instance is created only when getInstance() is called
# - No object exists until it is actually needed
# - Saves memory and startup cost


# Thread Safety: A Critical Concern in Singleton Pattern
# In a single-threaded environment, implementing a Singleton is straightforward. 
# However, things get complicated in multi-threaded applications, which are very common in modern software (especially web servers, mobile apps, etc.).

# The Problem
# Let's say two threads simultaneously call getInstance() for the first time in a lazy-loaded Singleton. 
# If the instance hasn't been created yet, both threads might pass the null check and end up creating two different instances — completely breaking the Singleton guarantee.

# ============================================================
# THREAD-SAFE SINGLETON PATTERNS
# ============================================================

# Problem:
# In a multi-threaded environment, two threads may enter
# getInstance() at the same time and create TWO instances.
# Thread safety ensures that ONLY ONE instance is ever created.

# ============================================================
# 1. SYNCHRONIZED METHOD (Thread-safe but slower)
# ============================================================

# Idea:
# - Lock the entire getInstance() method
# - Only ONE thread can execute it at a time
# - Simple but slower due to locking overhead

import threading

class SynchronizedSingleton:
    _instance = None
    _lock = threading.Lock()  # Class-level lock

    def __init__(self):
        raise Exception("Use getInstance()")

    @staticmethod
    def getInstance():
        # Entire method is synchronized
        with SynchronizedSingleton._lock:
            if SynchronizedSingleton._instance is None:
                SynchronizedSingleton._instance = SynchronizedSingleton.__new__(SynchronizedSingleton)
        return SynchronizedSingleton._instance


# Explanation:
# - Lock ensures only one thread can enter this block
# - Guarantees thread safety
# - Performance cost because lock is acquired on EVERY call

# ============================================================
# 2. DOUBLE-CHECKED LOCKING (Better performance)
# ============================================================

# Idea:
# - First check WITHOUT lock (fast path)
# - Lock only when instance is actually None
# - Second check inside lock to avoid race condition

class DoubleCheckedSingleton:
    _instance = None
    _lock = threading.Lock()

    def __init__(self):
        raise Exception("Use getInstance()")

    @staticmethod
    def getInstance():
        # First check (no locking)
        if DoubleCheckedSingleton._instance is None:
            with DoubleCheckedSingleton._lock:
                # Second check (with locking)
                if DoubleCheckedSingleton._instance is None:
                    DoubleCheckedSingleton._instance = DoubleCheckedSingleton.__new__(DoubleCheckedSingleton)
        return DoubleCheckedSingleton._instance


# Explanation:
# - Most calls skip locking once instance is created
# - Lock is acquired only during first initialization
# - Faster than synchronized method
# - More complex but commonly asked in interviews

# ============================================================
# 3. BILL PUGH SINGLETON (BEST PRACTICE – LAZY + THREAD-SAFE)
# ============================================================

# Idea:
# - Use a helper inner class
# - Instance is created ONLY when helper class is loaded
# - Class loading is thread-safe by design
# - No explicit locks required

class BillPughSingleton:

    def __init__(self):
        raise Exception("Use getInstance()")

    class _SingletonHelper:
        # Instance is created when this class is loaded
        INSTANCE = None

    @staticmethod
    def getInstance():
        if BillPughSingleton._SingletonHelper.INSTANCE is None:
            BillPughSingleton._SingletonHelper.INSTANCE = BillPughSingleton.__new__(BillPughSingleton)
        return BillPughSingleton._SingletonHelper.INSTANCE


# Explanation:
# - Inner helper class is NOT loaded until getInstance() is called
# - Python guarantees thread-safe class loading
# - Lazy initialization + thread safety
# - No synchronization overhead
# - Considered BEST PRACTICE for lazy singletons

# ============================================================
# COMPARISON SUMMARY (INTERVIEW-READY)
# ============================================================

# 1. Synchronized Method
# - Thread-safe: YES
# - Performance: SLOW
# - Simplicity: HIGH

# 2. Double-Checked Locking
# - Thread-safe: YES
# - Performance: GOOD
# - Complexity: MEDIUM

# 3. Bill Pugh Singleton
# - Thread-safe: YES
# - Lazy loading: YES
# - Performance: BEST
# - Recommended approach

# ============================================================
# ONE-LINE INTERVIEW ANSWERS
# ============================================================

# Synchronized Method:
# "Synchronizes the entire getInstance method to ensure thread safety."

# Double-Checked Locking:
# "Reduces synchronization overhead by locking only during initialization."

# Bill Pugh Singleton:
# "Uses class loading guarantees to achieve lazy, thread-safe initialization
# without explicit synchronization."
