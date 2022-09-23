import java.util.*;
import java.lang.*;
import static java.lang.Integer.*;

class Solution {
    
    private static Map<String, Integer> carFeeMap = new HashMap<>();
    private static Map<String, Integer> parkingLotMap = new HashMap<>();
    
    public int[] solution(int[] fees, String[] records) {
        final int basicTime = fees[0];
        final int basicFee = fees[1];
        final int unitTime = fees[2];
        final int unitFee = fees[3];
        
        for (String record : records) {
            final String[] unitRecord = record.split(" ");
            final String carNumber = unitRecord[1];
            final String status = unitRecord[2];
            final int minuteTime = calculateMinute(unitRecord[0]);
            // IN 이면 parkingLotMap에 추가
            if (status.equals("IN")) {
                parkingLotMap.put(carNumber, minuteTime);
            }
            // OUT 이면 계산 후 carFeeMap에 추가, parkingLotMap의 값 초기화
            if (status.equals("OUT")) {
                final int parkingTime = minuteTime - parkingLotMap.get(carNumber);
                // carFeeMap에 저장되어있으면 누적합, 없으면 추가
                if (carFeeMap.containsKey(carNumber)) {
                    carFeeMap.put(carNumber, carFeeMap.get(carNumber) + parkingTime);
                } else {
                    carFeeMap.put(carNumber, parkingTime);
                }
                parkingLotMap.remove(carNumber);
            }
        }
        for (String key : parkingLotMap.keySet()) {
            final int parkingTime = calculateMinute("23:59") - parkingLotMap.get(key);
            if (carFeeMap.containsKey(key)) {
                    carFeeMap.put(key, carFeeMap.get(key) + parkingTime);
                } else {
                    carFeeMap.put(key, parkingTime);
                }
        }
        final int[] answer = new int[carFeeMap.size()];
        final List<String> keySet = new ArrayList<>(carFeeMap.keySet());
        Collections.sort(keySet);
        int i = 0;
        for (String key : keySet) {
            final int parkingTime = carFeeMap.get(key);
            if (parkingTime <= basicTime) {
                answer[i] = basicFee;
                i++;
                continue;
            }
            answer[i] = basicFee + (int)(Math.ceil((parkingTime - basicTime) / (double)unitTime)) * unitFee;
            i++;
        }
        return answer;
    }
    
    private int calculateMinute(String time) {
        String[] times = time.split(":");
        final int hour = parseInt(times[0]);
        final int minute = parseInt(times[1]);
        return hour * 60 + minute;
    }
}
