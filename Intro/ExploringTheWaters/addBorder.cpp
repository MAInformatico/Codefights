std::vector<std::string> addBorder(std::vector<std::string> picture) {
    std::vector <std::string> data;    
    std::string border(picture[0].length() + 2, '*'); //first and last border
    data.push_back(border);
    for(int i = 0; i < picture.size(); ++i){
        data.push_back('*' + picture[i] + '*');
    }
    data.push_back(border);
return data;
}
