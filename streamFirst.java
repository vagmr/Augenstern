
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * @author vagmr
 * @version 0.0.1
 *          2023/6/29-14:39
 *          vagmrsTar
 */
public class streamFirst {
    public static void main(String[] args) {
        ArrayList<String> s2 = new ArrayList<>();
        Collections.addAll(s2, "老必当", "老对象", "老鹅", "爱迪生", "老圣诞节", "老家的绝对");
        OldMethod.CellctionAdjust(s2);
        OldMethod.StreamAdjust(s2);
    }
}

class OldMethod {
    public static void CellctionAdjust(List<String> ary) {
        List<String> ary2 = new ArrayList<>();
        for (String newAry : ary) {
            if (newAry.startsWith("老") && newAry.length() >= 2) {
                ary2.add(newAry);
            }
        }
        System.out.println(ary2);
    }

    // 使用stream流解决这个问题
    public static void StreamAdjust(List<String> ary) {
        // filter用来过滤使用lambda表达式，collect(Collectors.toList())收集到一个list集合中
        List<String> streamary = ary.stream().filter(s -> s.startsWith("老")).filter(a -> a.length() >= 3)
                .collect(Collectors.toList());
        System.out.println(streamary);
    }
}