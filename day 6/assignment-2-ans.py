# ─────────────────────────────────────────────
# Learning Management System (LMS)
# ─────────────────────────────────────────────

# ── Custom Exceptions ──────────────────────────────────────────────────────────

class LMSError(Exception):
    """Base exception for the LMS."""


class DuplicateEnrollmentError(LMSError):
    def __init__(self, student, course):
        super().__init__(f"{student.name} is already enrolled in '{course.title}'.")


class CourseFullError(LMSError):
    def __init__(self, course):
        super().__init__(f"'{course.title}' is full (max {course.capacity} students).")


class NotEnrolledError(LMSError):
    def __init__(self, student, course):
        super().__init__(f"{student.name} is not enrolled in '{course.title}'.")


class CourseNotFoundError(LMSError):
    def __init__(self, course_id):
        super().__init__(f"No course found with ID '{course_id}'.")


# ── Domain Classes ─────────────────────────────────────────────────────────────

class Instructor:
    def __init__(self, instructor_id: int, name: str, department: str):
        self.instructor_id = instructor_id
        self.name = name
        self.department = department

    # Magic methods
    def __repr__(self):
        return f"Instructor({self.instructor_id}, {self.name!r})"

    def __str__(self):
        return f"[Instructor #{self.instructor_id}] {self.name} — {self.department}"

    def __eq__(self, other):
        return isinstance(other, Instructor) and self.instructor_id == other.instructor_id

    def __hash__(self):
        return hash(self.instructor_id)


class Student:
    def __init__(self, student_id: int, name: str, email: str):
        self.student_id = student_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Student({self.student_id}, {self.name!r})"

    def __str__(self):
        return f"[Student #{self.student_id}] {self.name} <{self.email}>"

    def __eq__(self, other):
        return isinstance(other, Student) and self.student_id == other.student_id

    def __hash__(self):
        return hash(self.student_id)


class Course:
    def __init__(self, course_id: str, title: str, instructor: Instructor, capacity: int = 30):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.capacity = capacity

    def __repr__(self):
        return f"Course({self.course_id!r}, {self.title!r})"

    def __str__(self):
        return (
            f"[Course {self.course_id}] {self.title} "
            f"| Instructor: {self.instructor.name} "
            f"| Capacity: {self.capacity}"
        )

    def __eq__(self, other):
        return isinstance(other, Course) and self.course_id == other.course_id

    def __hash__(self):
        return hash(self.course_id)


# ── LMS (Enrollment Manager) ───────────────────────────────────────────────────

class LMS:
    """
    Central system that manages courses, students, and enrollments.

    Enrollment storage:
        _enrollments: dict[course_id -> list[Student]]
    """

    def __init__(self, name: str = "My LMS"):
        self.name = name
        self._courses: list[Course] = []
        self._students: list[Student] = []
        # key: course_id (str) → value: list of enrolled Student objects
        self._enrollments: dict[str, list[Student]] = {}

    # ── Repr ────────────────────────────────────────────────────────────────────
    def __repr__(self):
        return f"LMS({self.name!r}, courses={len(self._courses)}, students={len(self._students)})"

    def __str__(self):
        return f"=== {self.name} | {len(self._courses)} courses | {len(self._students)} students ==="

    def __len__(self):
        """Return total number of enrollments across all courses."""
        return sum(len(s) for s in self._enrollments.values())

    def __contains__(self, item):
        """Support 'course in lms' and 'student in lms' checks."""
        if isinstance(item, Course):
            return item in self._courses
        if isinstance(item, Student):
            return item in self._students
        return False

    # ── Course Management ───────────────────────────────────────────────────────
    def add_course(self, course: Course):
        if course not in self._courses:
            self._courses.append(course)
            self._enrollments[course.course_id] = []
            print(f"   Course added: {course}")

    def get_course(self, course_id: str) -> Course:
        for c in self._courses:
            if c.course_id == course_id:
                return c
        raise CourseNotFoundError(course_id)

    def list_courses(self):
        print(f"\n{'─'*55}")
        print(f"  COURSES IN {self.name.upper()}")
        print(f"{'─'*55}")
        if not self._courses:
            print("  (no courses yet)")
        for course in self._courses:
            enrolled = len(self._enrollments.get(course.course_id, []))
            print(f"  {course}  | Enrolled: {enrolled}/{course.capacity}")
        print(f"{'─'*55}\n")

    # ── Student Management ──────────────────────────────────────────────────────
    def add_student(self, student: Student):
        if student not in self._students:
            self._students.append(student)
            print(f"   Student added: {student}")

    def list_students(self):
        print(f"\n{'─'*55}")
        print("  ALL STUDENTS")
        print(f"{'─'*55}")
        if not self._students:
            print("  (no students yet)")
        for s in self._students:
            print(f"  {s}")
        print(f"{'─'*55}\n")

    # ── Enrollment ──────────────────────────────────────────────────────────────
    def enroll(self, student: Student, course_id: str):
        course = self.get_course(course_id)          # raises CourseNotFoundError
        enrolled = self._enrollments[course_id]

        if student in enrolled:
            raise DuplicateEnrollmentError(student, course)

        if len(enrolled) >= course.capacity:
            raise CourseFullError(course)

        enrolled.append(student)
        print(f"   {student.name} enrolled in '{course.title}'.")

    def unenroll(self, student: Student, course_id: str):
        course = self.get_course(course_id)
        enrolled = self._enrollments[course_id]

        if student not in enrolled:
            raise NotEnrolledError(student, course)

        enrolled.remove(student)
        print(f"   {student.name} unenrolled from '{course.title}'.")

    def list_students_in_course(self, course_id: str):
        course = self.get_course(course_id)
        enrolled = self._enrollments[course_id]

        print(f"\n{'─'*55}")
        print(f"  STUDENTS IN: {course.title} ({course_id})")
        print(f"{'─'*55}")
        if not enrolled:
            print("  (no students enrolled)")
        for s in enrolled:
            print(f"  {s}")
        print(f"{'─'*55}\n")

    def courses_for_student(self, student: Student):
        """List all courses a student is enrolled in."""
        print(f"\n{'─'*55}")
        print(f"  COURSES FOR: {student.name}")
        print(f"{'─'*55}")
        found = [c for c in self._courses if student in self._enrollments.get(c.course_id, [])]
        if not found:
            print("  (not enrolled in any course)")
        for c in found:
            print(f"  {c}")
        print(f"{'─'*55}\n")


# ── Test Data & Demo ───────────────────────────────────────────────────────────

def main():
    # ── Instructors ─────────────────────────────────────────────────────────────
    instructors = [
        Instructor(1, "Dr. Alice Mehta",   "Computer Science"),
        Instructor(2, "Prof. Brian Nair",  "Mathematics"),
        Instructor(3, "Dr. Carol D'Souza", "Data Science"),
    ]

    # ── Students ─────────────────────────────────────────────────────────────────
    students = [
        Student(101, "Ravi Kumar",    "ravi@example.com"),
        Student(102, "Priya Sharma",  "priya@example.com"),
        Student(103, "Arjun Patel",   "arjun@example.com"),
        Student(104, "Sneha Reddy",   "sneha@example.com"),
        Student(105, "Vikram Rao",    "vikram@example.com"),
    ]

    # ── Courses ───────────────────────────────────────────────────────────────────
    courses = [
        Course("CS101", "Intro to Python",        instructors[0], capacity=3),
        Course("MA201", "Linear Algebra",          instructors[1], capacity=30),
        Course("DS301", "Machine Learning Basics", instructors[2], capacity=30),
    ]

    # ── Set up LMS ────────────────────────────────────────────────────────────────
    lms = LMS("Academy LMS")
    print(f"\n{'═'*55}")
    print(f"  Setting up {lms.name}")
    print(f"{'═'*55}")

    print("\n-- Adding courses --")
    for c in courses:
        lms.add_course(c)

    print("\n-- Adding students --")
    for s in students:
        lms.add_student(s)

    # ── Enroll students ───────────────────────────────────────────────────────────
    print(f"\n{'═'*55}")
    print("  ENROLLMENTS")
    print(f"{'═'*55}")

    enrollments = [
        ("CS101", [students[0], students[1], students[2]]),   # fills capacity of 3
        ("MA201", [students[0], students[1], students[3], students[4]]),
        ("DS301", [students[2], students[3]]),
    ]

    for course_id, s_list in enrollments:
        for s in s_list:
            lms.enroll(s, course_id)

    # ── Exception demos ───────────────────────────────────────────────────────────
    print(f"\n{'═'*55}")
    print("  EXCEPTION HANDLING DEMOS")
    print(f"{'═'*55}")

    # 1. Duplicate enrollment
    try:
        lms.enroll(students[0], "CS101")
    except DuplicateEnrollmentError as e:
        print(f"   DuplicateEnrollmentError: {e}")

    # 2. Course full
    try:
        lms.enroll(students[3], "CS101")   # CS101 capacity=3, already full
    except CourseFullError as e:
        print(f"   CourseFullError: {e}")

    # 3. Course not found
    try:
        lms.enroll(students[0], "XX999")
    except CourseNotFoundError as e:
        print(f"   CourseNotFoundError: {e}")

    # 4. Unenroll someone not enrolled
    try:
        lms.unenroll(students[4], "CS101")
    except NotEnrolledError as e:
        print(f"  ✘ NotEnrolledError: {e}")

    # ── Listings ──────────────────────────────────────────────────────────────────
    print(f"\n{'═'*55}")
    print("  LISTINGS")
    print(f"{'═'*55}")

    lms.list_courses()

    lms.list_students_in_course("CS101")
    lms.list_students_in_course("MA201")
    lms.list_students_in_course("DS301")

    lms.list_students()

    lms.courses_for_student(students[0])   # Ravi

    # ── Magic method demos ────────────────────────────────────────────────────────
    print(f"{'═'*55}")
    print("  MAGIC METHOD DEMOS")
    print(f"{'═'*55}")
    print(f"  str(lms)          → {lms}")
    print(f"  repr(lms)         → {repr(lms)}")
    print(f"  len(lms)          → {len(lms)} total enrollments")
    print(f"  CS101 in lms      → {courses[0] in lms}")
    print(f"  students[0] in lms→ {students[0] in lms}")
    print(f"  repr(students[0]) → {repr(students[0])}")
    print(f"  repr(courses[0])  → {repr(courses[0])}")
    print(f"{'═'*55}\n")


if __name__ == "__main__":
    main()