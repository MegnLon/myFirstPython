#include<iostream>
using namespace  std;

class teacher{
private:
    int working_hour;
public:
    teacher(int x1=0):working_hour(x1){}
    virtual int get_mony()=0;
    void settime(int time){working_hour=time;}
    int get_time(){return working_hour;}
    virtual ~teacher(){}
};

class teacher_professor:public teacher{
private:
    static int basic_wages;
public:
    teacher_professor(int x1=0):teacher(x1){}
    int get_mony(){
        return (basic_wages+50*teacher::get_time());
    }
    virtual ~teacher_professor(){}
};
int teacher_professor::basic_wages=5000;

class teacher_adjprofessor:public teacher{
private:
    static int basic_wages;
public:
    teacher_adjprofessor(int x1=0):teacher(x1){}
    int get_mony(){
        return (basic_wages+30*teacher::get_time());
    }
    virtual ~teacher_adjprofessor(){}
};
int teacher_adjprofessor::basic_wages=3000;

class teacher_lecturer:public teacher{
private:
    static int basic_wages;
public:
    teacher_lecturer(int x1=0):teacher(x1){}
    int get_mony(){
        return (basic_wages+20*teacher::get_time());
    }
    virtual~teacher_lecturer(){}
};
int teacher_lecturer::basic_wages=2000;

void printchoice()
{
    cout<<"***********************************************************"<<endl;
    cout<<"Please input the teacher's professional ranks and titles."<<endl;
    cout<<"1.professor."<<endl;
    cout<<"2.adjprofessor."<<endl;
    cout<<"3.lecture."<<endl;
    cout<<"0.exit."<<endl;
    cout<<"***********************************************************"<<endl;
}

int main(){
    teacher *t=NULL;
    teacher_professor pro;
    cout<<"jiao shou de ji ben yue xin:"<<pro.get_mony()<<endl;

    teacher_adjprofessor proadj;
    cout<<"fu jiao shou de ji ben yue xin:"<<proadj.get_mony()<<endl;

    teacher_lecturer lec;
    cout<<"jiang shi de ji ben yue xin:"<<lec.get_mony()<<endl;

    int choice;
    int time;
    while(99){
        printchoice();
        cin>>choice;
        switch(choice){
        case 0:
            return 0;
            break;
        case 1:
            t=&pro;
            cout<<"Please input working time."<<endl;
            cin>>time;
            pro.settime(time);
            cout<<"jiao shou de yue xin:"<<t->get_mony()<<endl;
            break;
        case 2:
            t=&proadj;
            cout<<"Please input working time."<<endl;
            cin>>time;
            proadj.settime(time);
            cout<<"fu jiao shou de yue xin:"<<t->get_mony()<<endl;
            break;
        case 3:
            t=&lec;
            cout<<"Please input working time."<<endl;
            cin>>time;
            lec.settime(time);
            cout<<"jiang shi de yue xin:"<<t->get_mony()<<endl;
            break;
        default:
            cout<<"Iput error,please again."<<endl;
            break;
        }
    }
    return 0;
}
