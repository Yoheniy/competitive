class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        vector<double>result;
         double kelvin=celsius+273.15;
         double fahr=celsius*1.80+32.00;
         result.push_back(kelvin);
          result.push_back(fahr);
         return result;
    }
};