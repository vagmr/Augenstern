import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Stream {
    public static void main(String[] args) {
        List<Student> nb = new ArrayList<>();
        nb.add(new Student("xg", 28, 1.62));
        nb.add(new Student("Alice Anderson", 28, 1.62));
        nb.add(new Student("Bob Baker", 35, 1.78));
        nb.add(new Student("Catherine Clark", 43, 1.67));
        nb.add(new Student("Daniel Davis", 29, 1.85));
        nb.add(new Student("Emily Evans", 31, 1.73));
        nb.add(new Student("Frank Fisher", 36, 1.79));
        nb.add(new Student("Grace Garcia", 27, 1.61));
        nb.add(new Student("Henry Harris", 39, 1.77));
        nb.add(new Student("Isabella Jackson", 33, 1.69));
        nb.add(new Student("James Johnson", 45, 1.88));
        nb.stream().filter(s -> s.getAge() > 23 && s.getAge() < 37).sorted(Comparator.comparingInt(o -> o.age))
                .forEach(System.out::println);
    }
}

class Student {
    String name;
    int age;
    double height;

    public Student(String name, int age, double height) {
        this.age = age;
        this.height = height;
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    // 重写toString方法
    @Override
    public String toString() {
        return "Student [" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", height=" + height +
                ']';
    }

}
