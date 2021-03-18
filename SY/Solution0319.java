import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;

public class Solution0319 {

	public static void main(String[] args) {
		String genres[] = {"classic", "pop", "classic", "classic", "pop"};
		int plays[] = {500, 600, 150, 800, 2500};
		System.out.println(solution(genres, plays));
	}

	public static int[] solution(String[] genres, int[] plays) {

		ArrayList<Integer> result = new ArrayList<>();

		
		HashMap<String, ArrayList<Integer>> map = new HashMap<>();
		for (int i = 0; i < genres.length; i++) {
			if (map.containsKey(genres[i]) == false) {
				map.put(genres[i], new ArrayList<Integer>());
				map.get(genres[i]).add(0);
			}
			map.get(genres[i]).add(i);
			map.get(genres[i]).set(0, map.get(genres[i]).get(0) + plays[i]);
		}

		while (!map.isEmpty()) {
			String max_genre = Collections.max(map.entrySet(), Map.Entry.comparingByValue(new Comparator<ArrayList<Integer>>() {
				
				@Override
				public int compare(ArrayList<Integer> a, ArrayList<Integer> b) {
					if (a.get(0) > b.get(0))
						return 1;

					return 0;
				}
			})).getKey();

			for (int j = 0; j < 2; j++) {
				if( map.get(max_genre).size() == 1) {
					break;
				}
				int max_index = map.get(max_genre).get(1);
				int index = 1;
				for (int i = 2; i < map.get(max_genre).size() ; i++) {
					if (plays[max_index] < plays[map.get(max_genre).get(i)]) {
						max_index = map.get(max_genre).get(i);
						index = i;
					}
				}
				result.add(max_index);
				map.get(max_genre).remove(index);
			}
			map.remove(max_genre);
		}
		int[] array = new int[result.size()];
		int size=0;
		for(Integer temp : result){
		  array[size++] = temp;
		}


		return array;
	}

}
