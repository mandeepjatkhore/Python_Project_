# Python File Handling Tasks

## ✅ Task 1: Read a File and Handle Errors

### Objective:
Read data from a file and gracefully handle any errors such as:
- File not found
- Permission issues
- Unexpected read errors

### Instructions:
1. Create or ensure a file (e.g., `file.txt`) exists in your project directory.
2. Use a `try-except` block to:
   - Open the file in **read mode** (`"r"`).
   - Read its contents using `.read()` or `.readlines()`.
   - Handle exceptions like `FileNotFoundError` and print a user-friendly message.

---

## ✅ Task 2: Write and Append Data to a File

### Objective:
Demonstrate how to:
- Overwrite a file with new content
- Append new data without removing the existing content

### Instructions:
1. **Write Mode ("w")**:
   - Open a file using `"w"` mode.
   - Write some content.
   - This will erase the file's existing content.

2. **Append Mode ("a")**:
   - Open the file using `"a"` mode.
   - Add additional content without deleting what's already there.

3. Use `with open(...) as file:` block to ensure the file is closed properly.

4. You may verify the file content using a read operation.

---

## 💡 Tips:
- Use `"r"` for reading, `"w"` for writing, and `"a"` for appending.
- Always test the behavior by opening the file afterward to verify the changes.
