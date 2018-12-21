#include "Homework.hh"

#include <sstream>

#include "api/Packet.hh"
#include "api/PacketMissHandler.hh"
#include "oxm/openflow_basic.hh"
#include "types/ethaddr.hh"

#include "Controller.hh"
#include "SwitchConnection.hh"
#include "Flow.hh"
#include "Common.hh"

REGISTER_APPLICATION(Homework, {"controller", ""})

using namespace runos;


void Homework::init(Loader *loader, const Config &)
{
    Controller* ctrl = Controller::get(loader);

    LOG(INFO) << "Homework app init";

    uint8_t table_no = ctrl->reserveTable(); // Your must push flowmod in this table

    ctrl->registerHandler("homework",
    [=](SwitchConnectionPtr connection) {

        return [=](Packet& pkt, FlowPtr, Decision decision) {


            // Write your code here
            //Below example code

            LOG(INFO) << "PacketIn captured";

            ethaddr eth_dst = pkt.load(oxm::eth_dst());
			uint16_t vlan_id = 1;
			 try {
                vlan_id = pkt.load(ofb_vlan_vid);
            }
            catch(...) {
                LOG(INFO) << "some shit";
            }
			
            /*if (eth_dst.to_number() % 2 == 0){
              // I want to drop all packet that ended with zero bits
              of13::FlowMod fm;
              fm.command(of13::OFPFC_ADD);
              fm.table_id(table_no); //  Push your flow in this table
              fm.priority(1); // Priority must be higher than 0

              std::stringstream ss;
              ss << eth_dst;

              of13::EthDst* ethDstToFlowMod = new of13::EthDst(
                       EthAddress( ss.str() )
                    ); // Sorry for this

              fm.add_oxm_field(ethDstToFlowMod);
              connection->send(fm);
            }*/

            return decision;			
        };
    });
}
