#include<iostream>
using namespace std;

class rectangle {
	private:
		double length;
		double width;
	public:
		rectangle(double l,double w){
		    length=l;
		    width=w;
		}
		void showlength(){
			cout<<"矩形长度"<<length<<endl;
		}
		void showwidth(){
			cout<<"矩形长度"<<width<<endl;
		}
		
		double area(){
			return length*width;
		}
};
int main(){
	rectangle rect(99,89);
	
	rect.showlength();
	rect.showwidth();
	cout<<"矩形面积："<<rect.area()<<endl;
	
	return 0; 
}
