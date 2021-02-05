import java.util.ArrayList;

public class Cache {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        if(cacheSize == 0) {
            answer = 5 * cities.length;
        } else {
            ArrayList<String> cache = new ArrayList<String>();
            for(int inx = 0; inx < cities.length; inx++) {
                if(cache.contains(cities[inx].toUpperCase())) {
                    answer += 1;
                    cache.remove(cities[inx].toUpperCase());
                    cache.add(cities[inx].toUpperCase());
                } else if(cache.size() < cacheSize) {
                    answer += 5;
                    cache.add(cities[inx].toUpperCase());
                } else {
                    answer += 5;
                    cache.remove(0);
                    cache.add(cities[inx].toUpperCase());
                }
            }
        }
        return answer;
    }
}


